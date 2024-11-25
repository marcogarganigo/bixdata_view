from .alpha import *
from .businesslogic.models.table_settings import TableSettings
from .helper_view import *
from django.db.models import OuterRef, Subquery
from .businesslogic.settings_business_logic import *
from .businesslogic.models.record import *
from .businesslogic.models.field_settings import *
from django.contrib.auth.models import User
from .helpers.helperdb import *



@login_required(login_url='/login/')
def settings_table(request):
    hv = HelperView(request)
    users = SysUser.objects.all().values()
    hv.context['users'] = users
    return hv.render_template('admin_settings/table_settings/settings_table.html')


def settings_table_usertables(request):
    hv = HelperView(request)
    bl = SettingsBusinessLogic()
    userid = request.POST.get('userid')

    hv.context['workspaces'] = bl.get_user_tables(userid)
    return hv.render_template('admin_settings/table_settings/settings_table_user_tables.html')


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
    return hv.render_template('admin_settings/table_settings/settings_table_kanbanfields.html')


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
            [tableid, userid, title, tableid, userid, date, tableid, userid, user, tableid, userid, field1, tableid,
             userid, field2, tableid, userid, field3, tableid, userid, field4]
        )

    return HttpResponse({'success': True})


def settings_table_tablefields(request):
    tableid = request.POST.get('tableid')
    userid = request.POST.get('userid')
    fields_type = request.POST.get('fields_type')
    hv = HelperView(request)
    bl = SettingsBusinessLogic()
    hv.context['fields'] = bl.get_search_column_results(userid, tableid, fields_type)

    for field in hv.context['fields']:
        if field['fieldid'][-1] == '_':
            hv.context['fields'].remove(field)

    hv.context['fields_type'] = fields_type
    if fields_type == 'linked_columns':
        hv.context['linked_columns'] = list(SysTableLink.objects.filter(tablelinkid=tableid).values())
        hv.context['fields'] = ''
    return hv.render_template('admin_settings/table_settings/settings_table_column_search_results.html')


def settings_table_linkedtables(request):
    tableid = request.POST.get('tableid')
    userid = request.POST.get('userid')

    with connection.cursor() as cursor:
        cursor.execute(
            f"SELECT * FROM sys_table_link LEFT JOIN sys_user_order ON sys_table_link.tableid=sys_user_order.tableid AND sys_table_link.tablelinkid=sys_user_order.fieldid WHERE sys_table_link.tableid='{tableid}' ORDER BY sys_user_order.fieldorder ASC"
        )
        linked_tables = dictfetchall(cursor)

        orderNull = []
        orderNotNull = []

        for linked in linked_tables:
            if linked['fieldorder'] == None:
                orderNull.append(linked)
            else:
                orderNotNull.append(linked)

        linked_tables = orderNotNull
        linked_tables += orderNull

    hv = HelperView(request)
    hv.context['linkeds'] = linked_tables
    return hv.render_template('admin_settings/table_settings/settings_table_linkedtables.html')


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


def settings_table_linkedtables_save(request):
    tableid = request.POST.get('tableid')
    userid = request.POST.get('userid')

    fields = request.POST.get('orderArray')
    fields = json.loads(fields)
    order = 0

    with connection.cursor() as cursor:
        cursor.execute(
            "DELETE FROM sys_user_order WHERE userid=%s AND tableid=%s AND typepreference='keylabel'",
            [userid, tableid])

    for fieldid in fields:
        with connection.cursor() as cursor:
            cursor.execute("""
                  INSERT INTO sys_user_order (userid, tableid, fieldid, fieldorder, typepreference)
                  VALUES (%s, %s, %s, %s, %s)
              """, [userid, tableid, fieldid, order, 'keylabel'])

            order += 1

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

    return hv.render_template('admin_settings/table_settings/settings_table_column_search_results.html')


def settings_table_fieldsettings(request):
    fieldid = request.POST.get('fieldid')
    hv = HelperView(request)

    return hv.render_template('admin_settings/table_settings/settings_table_column_search_results_options.html')


def load_table_settings_menu(request):
    hv = HelperView(request)
    return hv.render_template('admin_settings/table_settings/settings_table_menu.html')


def settings_table_settings(request):
    tableid = request.POST.get('tableid')
    tablesettings_obj = TableSettings(tableid=tableid, userid=1)
    helperview_obj = HelperView(request)
    helperview_obj.context['tablesettings'] = tablesettings_obj.get_settings()

    return helperview_obj.render_template('admin_settings/table_settings/settings_table_settings.html')


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
    return hv.render_template('admin_settings/table_settings/settings_table_columnlinked.html')


def settings_table_columnlinked_save(request):
    return HttpResponse({'success': True})


def settings_table_fields(request):
    tableid = request.POST.get('tableid')
    userid = request.POST.get('userid')
    hv = HelperView(request)
    hv.context['fields'] = list(SysField.objects.filter(tableid=tableid).values())
    hv.context['tables'] = list(SysTable.objects.values())

    for field in hv.context['fields']:
        if field['fieldid'][-1] == '_':
            hv.context['fields'].remove(field)

    return hv.render_template('admin_settings/table_settings/settings_table_fields.html')


def settings_table_fields_settings_block(request):
    helper_view = HelperView(request)
    tableid = request.POST.get('tableid')
    fieldid = request.POST.get('fieldid')
    userid = int(request.POST.get('userid'))
    fieldsettings_obj = FieldSettings(tableid=tableid, fieldid=fieldid, userid=userid)
    helperview_obj = HelperView(request)

    with connection.cursor() as cursor:
        cursor.execute(
            f"SELECT * FROM sys_field WHERE tableid = '{tableid}' AND fieldid = '{fieldid}'"
        )
        record = dictfetchall(cursor)

        if record[0]['lookuptableid'] != '':
            cursor.execute(
                f"SELECT * FROM sys_lookup_table_item WHERE lookuptableid = '{record[0]['lookuptableid']}'"
            )
            items = dictfetchall(cursor)

    helperview_obj.context['fieldsettings'] = fieldsettings_obj.get_settings()
    helperview_obj.context['record'] = record
    if items:
        helperview_obj.context['items'] = items
    else:
        helperview_obj.context['items'] = ''

    # helperview_obj.context['fieldsettings'] = fieldsettings

    return helperview_obj.render_template('admin_settings/table_settings/settings_table_fields_settings_block.html')


def settings_table_fields_settings_fields_save(request):
    settings_list = request.POST.get('settings')

    settings_list = json.loads(settings_list)

    settings = request.POST.get('settings')
    userid = request.POST.get('userid')
    tableid = request.POST.get('tableid')
    field = request.POST.get('field')
    field_description = request.POST.get('field_description')
    field_label = request.POST.get('field_label')

    new_items = request.POST.get('newItems')
    new_items = json.loads(new_items)

    current_items = request.POST.get('currentItems')
    current_items = json.loads(current_items)

    deleted_items = request.POST.get('deletedItems')
    deleted_items = json.loads(deleted_items)

    lookuptableid = field + '_' + tableid

    for item in deleted_items:
        with connection.cursor() as cursor:
            cursor.execute(
                f"DELETE FROM sys_lookup_table_item WHERE lookuptableid = '{lookuptableid}' AND itemcode = '{item['itemcode']}'",
            )

    with connection.cursor() as cursor:
        cursor.execute(
            f"UPDATE sys_field SET description = '{field_description}', label = '{field_label}' WHERE tableid = '{tableid}' AND fieldid = '{field}'",
        )

    for item in new_items:
        with connection.cursor() as cursor:
            cursor.execute(
                f"INSERT INTO sys_lookup_table_item (lookuptableid, itemcode, itemdesc) VALUES ('{lookuptableid}', '{item['id']}', '{item['description']}')",
            )

    for item in current_items:
        with connection.cursor() as cursor:
            cursor.execute(
                f"UPDATE sys_lookup_table_item SET itemdesc = '{item['itemdesc']}' WHERE lookuptableid = '{lookuptableid}' AND itemcode = '{item['itemcode']}'",
            )

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
    return hv.render_template('admin_settings/table_settings/settings_table_fields_linked_table_fields.html')


def settings_table_fields_new_field(request):
    data = request.POST.get('serialized_data')
    data = json.loads(data)

    tableid = data['tableid']
    userid = data['userid']
    fieldid = data['fieldid']
    fielddescription = data['fielddescription']
    fieldtype = data['fieldtype']

    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT * FROM sys_field WHERE tableid= %s AND fieldid= %s", [tableid, fieldid]
        )
        row = dictfetchall(cursor)

        if not row:

            if fieldtype != 'Linked' and fieldtype != 'LongText':
                if fieldtype == 'Categoria':
                    cursor.execute(
                        "INSERT INTO sys_field (tableid, fieldid, description, lookuptableid, fieldtypeid, length, label) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                        [tableid, fieldid, fielddescription, fieldid + '_' + tableid, 'Parola', 255, 'Dati']
                    )
                if fieldtype == 'Checkbox':
                    cursor.execute(
                        "INSERT INTO sys_field (tableid, fieldid, description, lookuptableid, fieldtypeid, length, label, fieldtypewebid) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
                        [tableid, fieldid, fielddescription, fieldid + '_' + tableid, 'Parola', 255, 'Dati', 'checkbox']
                    )

                elif fieldtype in [ 'Numero', 'Parola', 'Memo', 'Utente']:
                    cursor.execute(
                        "INSERT INTO sys_field (tableid, fieldid, description, fieldtypeid, length, label) VALUES (%s, %s, %s, %s, %s, %s)",
                        [tableid, fieldid, fielddescription, fieldtype, 255, 'Dati']
                    )

                sql = f"ALTER TABLE user_{tableid} ADD COLUMN {fieldid} VARCHAR(255) NULL"

                if fieldtype == 'Data':
                    cursor.execute(
                        "INSERT INTO sys_field (tableid, fieldid, description, fieldtypeid, length, label) VALUES (%s, %s, %s, %s, %s, %s)",
                        [tableid, fieldid, fielddescription, 'Data', 255, 'Dati']
                    )

                    sql = f"ALTER TABLE user_{tableid} ADD COLUMN {fieldid} DATE NULL"


                cursor.execute(sql)

                if fieldtype == 'Categoria':

                    cursor.execute(
                        "INSERT INTO sys_lookup_table (description, tableid, itemtype, codelen, desclen) VALUES (%s, %s, %s, %s, %s)",
                        [fieldid, fieldid + '_' + tableid, 'Carattere', 255, 255]
                    )

                    values = data['valuesArray']

                    for value in values:
                        id = value['id']
                        description = value['description']

                        cursor.execute(
                            "INSERT INTO sys_lookup_table_item (lookuptableid, itemcode, itemdesc) VALUES (%s, %s, %s)",
                            [fieldid + '_' + tableid, description, description]
                        )
                    
                if fieldtype == 'Checkbox':
                    
                    cursor.execute(
                        "INSERT INTO sys_lookup_table (description, tableid, itemtype, codelen, desclen) VALUES (%s, %s, %s, %s, %s)",
                        [fieldid, fieldid + '_' + tableid, 'Carattere', 255, 255]
                    )

                    cursor.execute(
                        "INSERT INTO sys_lookup_table_item (lookuptableid, itemcode, itemdesc) VALUES (%s, %s, %s)",
                        [fieldid + '_' + tableid, 'Si', 'Si']
                    )

                    cursor.execute(
                        "INSERT INTO sys_lookup_table_item (lookuptableid, itemcode, itemdesc) VALUES (%s, %s, %s)",
                        [fieldid + '_' + tableid, 'No', 'No']
                    )

            elif fieldtype == 'LongText':


                cursor.execute(
                    "INSERT INTO sys_field (tableid, fieldid, description, fieldtypeid, length, label, fieldtypewebid) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                    [tableid, fieldid, fielddescription, 'Memo', 4294967295, 'Dati', 'html']
                )

                sql = f"ALTER TABLE user_{tableid} ADD COLUMN {fieldid} LONGTEXT NULL"

                cursor.execute(sql)


            else:

                linkedtableid = data['linkedtable']
                newcolumn = 'recordid' + linkedtableid + '_'
                newcolumn2 = '_recordid' + linkedtableid

                fieldid2 = 'recordid' + tableid + '_'

                fields = data['linkedtablefields']
                keyfieldlink = ''

                for field in fields:
                    keyfieldlink += field + ','

                keyfieldlink = keyfieldlink[:-1]

                sql = f"ALTER TABLE user_{tableid} ADD COLUMN {newcolumn} VARCHAR(255) NULL"

                sql2 = f"INSERT INTO sys_field (tableid, fieldid, description, fieldtypeid, length, label, keyfieldlink, tablelink) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
                params2 = [tableid, newcolumn, fielddescription, 'Parola', 255, linkedtableid, keyfieldlink,
                           linkedtableid]

                sql3 = f"INSERT INTO sys_field (tableid, fieldid, description, fieldtypeid, length, label, keyfieldlink, tablelink) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
                params3 = [linkedtableid, fieldid2, fielddescription, 'Parola', 255, tableid, keyfieldlink, tableid]

                sql4 = f"INSERT INTO sys_table_link (tableid, tablelinkid) VALUES (%s, %s)"
                params4 = [linkedtableid, tableid]

                sql5 = f"ALTER TABLE user_{tableid} ADD COLUMN {newcolumn2} VARCHAR(255) NULL"

                sql6 = f"INSERT INTO sys_field (tableid, fieldid, description, fieldtypeid, length, label, keyfieldlink, tablelink) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
                params6 = [tableid, newcolumn2, fielddescription, 'Parola', 255, 'Dati', keyfieldlink, linkedtableid]

                with connection.cursor() as cursor:
                    cursor.execute(sql)
                    cursor.execute(sql2, params2)
                    cursor.execute(sql3, params3)
                    cursor.execute(sql4, params4)
                    cursor.execute(sql5)
                    cursor.execute(sql6, params6)

    return JsonResponse({'success': True})


def load_category_fields(request):
    tableid = request.POST.get('tableid')

    sql = f"SELECT * FROM sys_lookup_table_item WHERE tableid LIKE %'{tableid}'%"

    with connection.cursor() as cursor:
        cursor.execute(
            f"SELECT * FROM sys_lookup_table_item WHERE lookuptableid LIKE '%{tableid}%'"
        )
        fields = dictfetchall(cursor)

    hv = HelperView(request)
    hv.context['fields'] = fields
    return hv.render_template('admin_settings/category_fields.html')


def settings_table_newtable(request):
    return render(request, 'admin_settings/table_settings/newtable.html')


def save_newtable(request):
    tableid = request.POST.get('tableid')
    description = request.POST.get('description')

    with connection.cursor() as cursor:
        cursor.execute(
            f"SELECT * FROM sys_table WHERE id='{tableid}'",
        )
        table = dictfetchall(cursor)

        if not table:
            cursor.execute(
                f"INSERT INTO sys_table (id, description, workspace) VALUES ('{tableid}', '{description}', 'ALTRO')"

            )

            cursor.execute(
                f"CREATE TABLE user_{tableid} ( recordid_ CHAR(32) PRIMARY KEY, creatorid_ INT(11) NOT NULL, creation_ DATETIME NOT NULL, lastupdaterid_ INT(11), lastupdate_ DATETIME, totpages_ INT(11), firstpagefilename_ VARCHAR(255), recordstatus_ VARCHAR(255), deleted_ CHAR(1) DEFAULT 'N', id INT(11) ) CHARACTER SET utf8 COLLATE utf8_general_ci"
            )

            cursor.execute(
                f"INSERT INTO sys_field (tableid, fieldid, fieldtypeid, label, description) VALUES ('{tableid}', 'id', 'Seriale', 'Sistema', 'ID')"
            )

            cursor.execute(
                f"SELECT id from sys_field WHERE tableid='{tableid}' AND fieldid='id'"
            )

            fieldid = dictfetchall(cursor)[0]['id']

            cursor.execute(
                f"INSERT INTO sys_user_field_order (userid, tableid, fieldid, fieldorder, typepreference ) VALUES (1, '{tableid}', '{fieldid}', 0, 'search_results_fields')"
            )

            cursor.execute(
                f"INSERT INTO sys_user_field_order (userid, tableid, fieldid, fieldorder, typepreference ) VALUES (1, '{tableid}', '{fieldid}', 0, 'insert_fields')"
            )

            cursor.execute(
                f"INSERT INTO sys_user_field_order (userid, tableid, fieldid, fieldorder, typepreference ) VALUES (1, '{tableid}', '{fieldid}', 0, 'search_fields')"
            )

            cursor.execute(
                f"INSERT INTO sys_view (name, userid, tableid, query_conditions) VALUES ('Tutti', 1, '{tableid}', 'true')"
            )

            cursor.execute(
                f"SELECT id from sys_view WHERE tableid='{tableid}' AND name='Tutti'"
            )
            viewid = dictfetchall(cursor)[0]['id']

            cursor.execute(
                f"INSERT INTO sys_user_table_settings (userid, tableid , settingid, value) VALUES (1, '{tableid}', 'default_viewid', '{viewid}')"
            )

            cursor.execute(
                f"INSERT INTO sys_user_table_settings (userid, tableid , settingid, value) VALUES (1, '{tableid}', 'default_recordtab', 'Fields')"
            )

    return JsonResponse({'success': True})


@login_required(login_url='/login/')
def settings_user(request):
    hv = HelperView(request)
    users = Helperdb.sql_query("SELECT * FROM sys_user")


    groups = []

    for user in users:
        if user['description'] == 'Gruppo':
            users.remove(user)
            groups.append(user)

    hv.context['users'] = users
    hv.context['groups'] = groups

    return hv.render_template('admin_settings/user_settings/settings_user.html')


def settings_user_newuser(request):
    return render(request, 'admin_settings/user_settings/newuser.html')


def save_newuser(request):
    firstname = request.POST.get('firstname')
    lastname = request.POST.get('lastname')
    password = request.POST.get('password')
    email = request.POST.get('email')

    username = firstname.lower() + '.' + lastname.lower()

    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT * FROM auth_user WHERE username = %s", [username]
        )
        user = dictfetchall(cursor)

        if user:
            return JsonResponse({'success': False})
        else:

            user = User.objects.create_user(
                username=username,
                password=password,
                first_name=firstname,
                last_name=lastname,
                email=email
            )
            bixid = user.id

            sql =  "INSERT INTO sys_user (firstname, lastname, username, disabled, superuser, bixid) VALUES (%s, %s, %s, 'N', 'N', %s)",[firstname, lastname, username, bixid]

            Hv = HelperView(request)
            userid = Hv.create_new_userid()

            with connection.cursor() as cursor:
                cursor.execute(
                    "INSERT INTO sys_user (id, firstname, lastname, username, disabled, superuser, bixid) VALUES (%s, %s, %s, %s, 'N', 'N', %s)",
                    [userid, firstname, lastname, username, bixid]
                )

            return JsonResponse({'success': True})


def settings_user_newgroup(request):

    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT * FROM sys_user"
        )
        users = dictfetchall(cursor)
    return render(request, 'admin_settings/newgroup.html')


def save_newgroup(request):
    groupname = request.POST.get('name')
    groupusername = request.POST.get('username')

    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT * FROM sys_user WHERE username = %s", [groupusername]
        )
        user = dictfetchall(cursor)


        if not user:
            Hv = HelperView(request)
            userid = Hv.create_new_userid()

            cursor.execute(
                "INSERT INTO sys_user (id, firstname, description, username) VALUES (%s, %s, %s, %s)", [userid, groupname, 'Gruppo', groupusername]
            )

    return JsonResponse({'success': True})


def get_group_settings(request):

    context = {}

    groupusername = request.POST.get('groupusername')

    groupid = Helperdb.sql_query(f"SELECT id FROM sys_user WHERE username = '{groupusername}'")

    groupid = groupid[0]['id']


    group_users = Helperdb.sql_query(f"SELECT userid FROM sys_group_user WHERE groupid = {groupid}")

    users_selected = []

    if group_users:
        for user in group_users:
            selected_users = Helperdb.sql_query(
                f"SELECT * FROM sys_user WHERE id = {user['userid']} AND description != 'Gruppo'")
            users_selected.extend(selected_users)

        users = Helperdb.sql_query("SELECT * FROM sys_user WHERE description != 'Gruppo'")

        for user_selected in users_selected:
            users = [user for user in users if user['id'] != user_selected['id']]


    else:
        users = Helperdb.sql_query("SELECT * FROM sys_user WHERE description != 'Gruppo'")
        users_selected = []

    context['users'] = users
    context['users_selected'] = users_selected
    context['groupid'] = groupid


    return render(request, 'admin_settings/group_settings.html', context)


def save_group_users(request):
    selected_users = request.POST.get('selectedUsers')
    selected_users = json.loads(selected_users)

    groupid = request.POST.get('groupid')

    Helperdb.sql_execute(f"DELETE FROM sys_group_user WHERE groupid = {groupid}")

    if selected_users:
        for user in selected_users:
            Helperdb.sql_execute(f"INSERT INTO sys_group_user (groupid, userid) VALUES ({groupid}, {user})")





    return JsonResponse({'success': True})