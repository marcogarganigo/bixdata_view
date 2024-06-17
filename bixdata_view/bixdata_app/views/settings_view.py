from .alpha import *
from .businesslogic.models.table_settings import TableSettings
from .helper_view import *
from django.db.models import OuterRef, Subquery
from .businesslogic.settings_business_logic import *
from .businesslogic.models.record import *
from .businesslogic.models.field_settings import *


@login_required(login_url='/login/')
def settings_table(request):
    hv = HelperView(request)
    users = SysUser.objects.all().values()
    hv.context['users'] = users
    return hv.render_template('admin_settings/settings_table.html')


def settings_table_usertables(request):
    hv = HelperView(request)
    bl = SettingsBusinessLogic()
    userid = request.POST.get('userid')

    hv.context['workspaces'] = bl.get_user_tables(userid)
    return hv.render_template('admin_settings/settings_table_user_tables.html')


def settings_table_usertables_save(request):
    userid = request.POST.get('userid')
    SysUserTableOrder.objects.filter(userid=userid, typepreference='menu').delete()

    workspaces = request.POST.get('tables')
    workspaces = json.loads(workspaces)
    order = 0;
    for workspace in workspaces:
        workspace_name = workspace['workspace']
        tables = workspace['tables']
        for tableid in tables:
            t = SysTable.objects.get(id=tableid)
            t.workspace = workspace_name
            t.save()
            t = SysUserTableOrder(userid=SysUser.objects.get(id=userid), tableid=SysTable.objects.get(id=tableid),
                                  typepreference='menu', tableorder=order)
            t.save()
            order += 1

    return JsonResponse({'success': True})


def settings_table_admin(request):
    tableid = request.POST.get('tableid')
    return HttpResponse('test')


def settings_table_kanbanfields(request):
    tableid = request.POST.get('tableid')
    userid = request.POST.get('userid')

    sql = f"SELECT * FROM sys_user_table_settings WHERE tableid = '{tableid}' AND settingid LIKE 'kanban_%' AND userid = '{userid}'"
    with connection.cursor() as cursor:
        cursor.execute(sql)
        settings = dictfetchall(cursor)


    sql = f"SELECT * FROM sys_field WHERE tableid = '{tableid}'"

    with connection.cursor() as cursor:
        cursor.execute(sql)
        fields = dictfetchall(cursor)

    selected_fields = {}
    for setting in settings:
        for field in fields:
            if setting["value"] == field["fieldid"]:
                field["selected"] = True
                selected_fields[setting["settingid"]] = field['fieldid']

    fields_by_type = {}

    for field in fields:
        fieldtypeid = field["fieldtypeid"]

        if fieldtypeid not in fields_by_type:
            fields_by_type[fieldtypeid] = []

        fields_by_type[fieldtypeid].append(field)

    hv = HelperView(request)
    hv.context['fields'] = fields_by_type
    hv.context['selected_fields'] = selected_fields
    return hv.render_template('admin_settings/settings_table_kanbanfields.html')

def settings_table_kanbanfields_save(request):
    tableid = request.POST.get('tableid')
    userid = request.POST.get('userid')
    title = request.POST.get('title')
    date = request.POST.get('date')
    user = request.POST.get('user')
    field1 = request.POST.get('field1')
    field2 = request.POST.get('field2')
    field3 = request.POST.get('field3')
    field4 = request.POST.get('field4')

    with connection.cursor() as cursor:
        cursor.execute(
            f"DELETE FROM sys_user_table_settings WHERE tableid = '{tableid}' AND userid = '{userid}' AND (settingid = 'kanban_title' OR settingid = 'kanban_date' OR settingid = 'kanban_user' OR settingid = 'kanban_field1' OR settingid = 'kanban_field2' OR settingid = 'kanban_field3' OR settingid = 'kanban_field4')",
        )

        cursor.execute(
            "INSERT INTO sys_user_table_settings (tableid, userid, settingid, value) VALUES (%s, %s, 'kanban_title', %s), (%s, %s, 'kanban_date', %s), (%s, %s, 'kanban_user', %s), (%s, %s, 'kanban_field1', %s), (%s, %s, 'kanban_field2', %s), (%s, %s, 'kanban_field3', %s), (%s, %s, 'kanban_field4', %s)",
            [tableid, userid, title, tableid, userid, date, tableid, userid, user, tableid, userid, field1, tableid, userid, field2, tableid, userid, field3, tableid, userid, field4]
        )

    return HttpResponse({'success': True})


def settings_table_tablefields(request):
    tableid = request.POST.get('tableid')
    userid = request.POST.get('userid')
    fields_type = request.POST.get('fields_type')
    hv = HelperView(request)
    bl = SettingsBusinessLogic()
    hv.context['fields'] = bl.get_search_column_results(userid, tableid, fields_type)
    hv.context['fields_type'] = fields_type
    if fields_type == 'linked_columns':
        hv.context['linked_columns'] = list(SysTableLink.objects.filter(tablelinkid=tableid).values())
        hv.context['fields'] = ''
    return hv.render_template('admin_settings/settings_table_column_search_results.html')


def settings_table_tablefields_save(request):
    tableid = request.POST.get('tableid')
    userid = request.POST.get('userid')
    fields_type = request.POST.get('fields_type')
    master_tableid = request.POST.get('master_tableid')
    if fields_type == 'linked_columns':
        SysUserFieldOrder.objects.filter(userid=userid, tableid=tableid, typepreference=fields_type,
                                         master_tableid=master_tableid).delete()
    else:
        SysUserFieldOrder.objects.filter(userid=userid, tableid=tableid, typepreference=fields_type).delete()

    fields = request.POST.get('orderArray')
    fields = json.loads(fields)
    order = 0;
    for fieldid in fields:
        user = SysUser.objects.get(id=userid)
        table = SysTable.objects.get(id=tableid)
        field = SysField.objects.get(id=fieldid)
        if fields_type == 'linked_columns':
            with connection.cursor() as cursor:
                cursor.execute("""
                      INSERT INTO sys_user_field_order (userid, tableid, fieldid, typepreference, fieldorder, master_tableid)
                      VALUES (%s, %s, %s, %s, %s, %s)
                  """, [userid, tableid, fieldid, fields_type, order, master_tableid])
        else:
            with connection.cursor() as cursor:
                cursor.execute("""
                      INSERT INTO sys_user_field_order (userid, tableid, fieldid, typepreference, fieldorder)
                      VALUES (%s, %s, %s, %s, %s)
                  """, [userid, tableid, fieldid, fields_type, order])

        order += 1

    if userid == '1':
        with connection.cursor() as cursor:
            cursor.execute(
                "DELETE FROM sys_user_column_width WHERE tableid=%s",
                [tableid])
    else:
        with connection.cursor() as cursor:
            cursor.execute(
                "DELETE FROM sys_user_column_width WHERE userid=%s AND tableid=%s",
                [userid, tableid])

    return HttpResponse({'success': True})


def master_columns(request):
    master_tableid = request.POST.get('master_tableid')
    tableid = request.POST.get('tableid')
    typepreference = request.POST.get('typepreference')
    userid = 1

    hv = HelperView(request)

    with connection.cursor() as cursor:
        cursor.execute('SELECT * FROM sys_field WHERE sys_field.tableid=%s ORDER BY fieldid', [tableid])
        fields = dictfetchall(cursor)

        cursor.execute(
            'SELECT * FROM sys_user_field_order AS t WHERE t.tableid=%s AND t.typepreference=%s AND t.master_tableid=%s ORDER BY fieldorder asc',
            [tableid, typepreference, master_tableid])
        visible_fields = dictfetchall(cursor)

    for field in fields:
        field['fieldorder'] = None

    if visible_fields is not None:
        for visible_field in visible_fields:
            for field in fields:
                if visible_field['fieldid'] == field['id']:
                    del fields[fields.index(field)]
                    visible_field['id'] = field['id']
                    visible_field['description'] = field['description']
                    visible_field['label'] = field['label']

    fields = visible_fields + fields

    hv.context['fields'] = fields

    return hv.render_template('admin_settings/settings_table_column_search_results.html')


def settings_table_fieldsettings(request):
    fieldid = request.POST.get('fieldid')
    hv = HelperView(request)

    return hv.render_template('admin_settings/settings_table_column_search_results_options.html')


def load_table_settings_menu(request):
    hv = HelperView(request)
    return hv.render_template('admin_settings/settings_table_menu.html')


def settings_table_settings(request):
    tableid = request.POST.get('tableid')
    tablesettings_obj = TableSettings(tableid=tableid, userid=1)
    helperview_obj = HelperView(request)
    helperview_obj.context['tablesettings'] = tablesettings_obj.get_settings()

    return helperview_obj.render_template('admin_settings/settings_table_settings.html')


def settings_table_fields_settings_save(request):
    settings_list = request.POST.get('settings')

    settings_list = json.loads(settings_list)

    userid = request.POST.get('userid')
    tableid = request.POST.get('tableid')

    tablesettings_obj = TableSettings(tableid=tableid, userid=1)
    # esempio fieldsettings_obj.settings['obbligatorio']['value']=True
    # esempio fieldsettings_obj.save()
    # dict con tutt i i settings. vedi te come compilarlo fieldsettings_obj.settings

    for setting in settings_list:
        tablesettings_obj.settings[setting['name']]['value'] = setting['value']

    tablesettings_obj.save()

    return HttpResponse({'success': True})


def settings_table_columnlinked(request):
    fields_type = 'linked_table_fields'
    userid = request.POST.get('userid')
    tableid = request.POST.get('tableid')
    hv = HelperView(request)
    linked_tables = list(SysTableLink.objects.filter(tablelinkid=tableid).values())
    linked_tables2 = list()
    for linked_table in linked_tables:
        linked_tables2.append(linked_table['tableid_id'])
    hv.context['linked_tables'] = linked_tables2
    bl = SettingsBusinessLogic()
    hv.context['fields'] = bl.get_search_column_results(userid, tableid, fields_type)
    return hv.render_template('admin_settings/settings_table_columnlinked.html')


def settings_table_columnlinked_save(request):
    return HttpResponse({'success': True})


def settings_table_fields(request):
    tableid = request.POST.get('tableid')
    userid = request.POST.get('userid')
    hv = HelperView(request)
    hv.context['fields'] = list(SysField.objects.filter(tableid=tableid).values())
    hv.context['tables'] = list(SysTable.objects.values())
    return hv.render_template('admin_settings/settings_table_fields.html')


def settings_table_fields_settings_block(request):
    helper_view = HelperView(request)
    tableid = request.POST.get('tableid')
    fieldid = request.POST.get('fieldid')
    userid = int(request.POST.get('userid'))
    fieldsettings_obj = FieldSettings(tableid=tableid, fieldid=fieldid, userid=userid)
    helperview_obj = HelperView(request)

    helperview_obj.context['fieldsettings'] = fieldsettings_obj.get_settings()
    # helperview_obj.context['fieldsettings'] = fieldsettings

    return helperview_obj.render_template('admin_settings/settings_table_fields_settings_block.html')


def settings_table_fields_settings_fields_save(request):
    settings_list = request.POST.get('settings')

    settings_list = json.loads(settings_list)

    settings = request.POST.get('settings')
    userid = request.POST.get('userid')
    tableid = request.POST.get('tableid')
    field = request.POST.get('field')

    fieldsettings_obj = FieldSettings(tableid=tableid, fieldid=field, userid=userid)
    # esempio fieldsettings_obj.settings['obbligatorio']['value']=True
    # esempio fieldsettings_obj.save()
    # dict con tutt i i settings. vedi te come compilarlo fieldsettings_obj.settings

    for setting in settings_list:
        fieldsettings_obj.settings[setting['name']]['value'] = setting['value']

    fieldsettings_obj.save()

    return HttpResponse({'success': True})


def settings_table_fields_linked_table(request):
    tableid = request.POST.get('tableid')
    hv = HelperView(request)
    hv.context['fields'] = list(SysField.objects.filter(tableid=tableid).values())
    return hv.render_template('admin_settings/settings_table_fields_linked_table_fields.html')


def settings_table_fields_new_field(request):
    data = request.POST.get('serialized_data')
    data = json.loads(data)

    tableid = data['tableid']
    userid = data['userid']
    fieldid = data['fieldid']
    fielddescription = data['fielddescription']
    fieldtype = data['fieldtype']

    return HttpResponse({'success': True})
