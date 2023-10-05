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


def settings_table_columnsearchresults(request):
    tableid = request.POST.get('tableid')
    userid = request.POST.get('userid')
    hv = HelperView(request)
    bl = SettingsBusinessLogic()
    hv.context['fields'] = bl.get_search_column_results(userid, tableid)
    return hv.render_template('admin_settings/settings_table_column_search_results.html')


def settings_table_columnsearchresults_save(request):
    tableid= request.POST.get('tableid')
    userid = request.POST.get('userid')
    SysUserFieldOrder.objects.filter(userid=userid, tableid=tableid, typepreference='columnsearchresults').delete()
    fields = request.POST.get('orderArray')
    fields = json.loads(fields)
    order = 0;
    for fieldid in fields:
        user=SysUser.objects.get(id=userid)
        table=SysTable.objects.get(id=tableid)
        field=SysField.objects.get(id=fieldid)
        t = SysUserFieldOrder(userid=user, tableid=table, fieldid=field, typepreference='columnsearchresults', fieldorder=order)
        t.save()
        order += 1
    return HttpResponse({'success': True})


def settings_table_fieldsettings(request):
    fieldid = request.POST.get('fieldid')
    hv = HelperView(request)

    return hv.render_template('admin_settings/settings_table_column_search_results_options.html')
