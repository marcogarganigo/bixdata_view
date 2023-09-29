from .alpha import *
from .helper_view import *
from django.db.models import OuterRef, Subquery
from .businesslogic.settings_business_logic import *

@login_required(login_url='/login/')
def settings_table(request):
    hv=HelperView(request)
    users = SysUser.objects.all().values()
    hv.context['users']=users
    return hv.render_template('admin_settings/settings_table.html')
    

def settings_table_user_tables(request):
    hv=HelperView(request)
    bl=SettingsBusinessLogic()
    userid=request.POST.get('userid')
    
    hv.context['workspaces']=bl.get_user_tables(userid)  
    return hv.render_template('admin_settings/settings_table_user_tables.html')


def save_table_settings(request):


    SysUserTableOrder.objects.filter(userid=1, typepreference='menu').delete()

    workspaces = request.POST.get('tables')
    workspaces=json.loads(workspaces)
    order=0;
    for workspace in workspaces:
        workspace_name=workspace['workspace']
        tables=workspace['tables']
        for tableid in tables:
            t=SysTable.objects.get(id=tableid)
            t.workspace=workspace_name
            t.save()
            t=SysUserTableOrder(userid=SysUser.objects.get(id=1),tableid=SysTable.objects.get(id=tableid),typepreference='menu',tableorder=order)
            t.save()
            order+=1

    return JsonResponse({'success': True})


def settings_table_admin(request):
    tableid = request.POST.get('tableid')
    return HttpResponse('test')