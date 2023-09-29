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
    
    returned=bl.get_user_tables()  
    hv.context['tables']=returned['tables']
    hv.context['workspaces']=returned['workspaces']
    return hv.render_template('admin_settings/settings_table_user_tables.html')


def save_table_settings(request):


    SysUserTableOrder.objects.filter(userid=1, typepreference='menu').delete()

    tables = request.POST.get('tables')
    tables=json.loads(tables)
    order=0;
    for tableid in tables:
        x=SysUserTableOrder(userid=SysUser.objects.get(id=1),tableid=SysTable.objects.get(id=tableid),typepreference='menu',tableorder=order)
        x.save()
        order+=1

    return JsonResponse({'success': True})


def settings_table_admin(request):
    tableid = request.POST.get('tableid')
    return HttpResponse('test')