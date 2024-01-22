from .alpha import *
from .helper_view import *
from django.db.models import OuterRef, Subquery
from .businesslogic.settings_business_logic import *


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
    SysUserTableOrder.objects.filter(userid=1, typepreference='menu').delete()

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
            t = SysUserTableOrder(userid=SysUser.objects.get(id=1), tableid=SysTable.objects.get(id=tableid),typepreference='menu', tableorder=order)
            t.save()
            order += 1

    return JsonResponse({'success': True})


def settings_table_admin(request):
    tableid = request.POST.get('tableid')
    return HttpResponse('test')


def settings_table_tablefields(request):
    tableid = request.POST.get('tableid')
    userid = request.POST.get('userid')
    fields_type = request.POST.get('fields_type')
    hv = HelperView(request)
    bl = SettingsBusinessLogic()
    hv.context['fields'] = bl.get_search_column_results(userid, tableid, fields_type)
    return hv.render_template('admin_settings/settings_table_column_search_results.html')


def settings_table_tablefields_save(request):
    tableid= request.POST.get('tableid')
    userid = request.POST.get('userid')
    fields_type = request.POST.get('fields_type')
    SysUserFieldOrder.objects.filter(userid=userid, tableid=tableid, typepreference=fields_type).delete()
    fields = request.POST.get('orderArray')
    fields = json.loads(fields)
    order = 0;
    for fieldid in fields:
        user=SysUser.objects.get(id=userid)
        table=SysTable.objects.get(id=tableid)
        field=SysField.objects.get(id=fieldid)
        t = SysUserFieldOrder(userid=user, tableid=table, fieldid=field, typepreference=fields_type, fieldorder=order)
        t.save()
        order += 1
    return HttpResponse({'success': True})

def settings_table_fieldsettings(request):
    fieldid = request.POST.get('fieldid')
    hv = HelperView(request)

    return hv.render_template('admin_settings/settings_table_column_search_results_options.html')

def load_table_settings_menu(request):
    hv = HelperView(request)
    return hv.render_template('admin_settings/settings_table_menu.html')

def settings_table_settings(request):
    hv = HelperView(request)
    return hv.render_template('admin_settings/settings_table_settings.html')

def settings_table_fields_settings_save(request):
    settings = request.POST.get('settings')
    userid = request.POST.get('userid')
    tableid = request.POST.get('tableid')

    settings_list = json.loads(settings)

    with connection.cursor() as cursor:
        for setting in settings_list:
            cursor.execute(
                "SELECT * FROM sys_user_table_settings WHERE userid = %s AND settingid = %s and tableid = %s",
                [userid, setting['name'], tableid]
            )
            existing_setting = cursor.fetchone()

            if existing_setting:
                cursor.execute(
                    "UPDATE sys_user_table_settings SET value = %s WHERE userid = %s AND settingid = %s and tableid = %s",
                    [setting['value'], userid, setting['name'], tableid]
                )
            else:
                cursor.execute(
                    "INSERT INTO sys_user_table_settings (userid, tableid, settingid, value) VALUES (%s, %s, %s, %s)",
                    [userid, tableid, setting['name'], setting['value']]
                )
    return HttpResponse({'success': True})


def settings_table_columnlinked(request):
    fields_type = 'linked_table_fields'
    userid = request.POST.get('userid')
    tableid = request.POST.get('tableid')
    hv=HelperView(request)
    linked_tables=list(SysTableLink.objects.filter(tablelinkid=tableid).values())
    linked_tables2=list()
    for linked_table in linked_tables:
        linked_tables2.append(linked_table['tableid_id'])
    hv.context['linked_tables']=linked_tables2
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
    return hv.render_template('admin_settings/settings_table_fields.html')


def settings_table_fields_settings_block(request):
    hv = HelperView(request)
    return hv.render_template('admin_settings/settings_table_fields_settings_block.html')

def settings_table_fields_settings_fields_save(request):

    settings = request.POST.get('settings')
    userid = request.POST.get('userid')
    tableid = request.POST.get('tableid')
    field = request.POST.get('field')

    settings_list = json.loads(settings)

    with connection.cursor() as cursor:
        for setting in settings_list:
            cursor.execute(
                "SELECT * FROM sys_user_field_settings WHERE userid = %s AND fieldid = %s and settingid = %s and tableid = %s",
                [userid, field, setting['name'], tableid]
            )
            existing_setting = cursor.fetchone()

            if existing_setting:
                cursor.execute(
                    "UPDATE sys_user_field_settings SET value  = %s where tableid = %s AND userid = %s AND fieldid = %s and settingid = %s",
                    [setting['value'], tableid, userid, field, setting['name']]
                )
            else:
                cursor.execute(
                    "INSERT INTO sys_user_field_settings (userid, tableid, fieldid, settingid, value) VALUES (%s, %s, %s, %s, %s)",
                    [userid, tableid, field, setting['name'], setting['value']]
                )
    return HttpResponse({'success': True})