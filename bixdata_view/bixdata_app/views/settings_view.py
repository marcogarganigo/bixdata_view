from .alpha import *
from .helper_view import *
from django.db.models import OuterRef, Subquery
from .businesslogic.settings_business_logic import *

@login_required(login_url='/login/')
def settings_table(request):
    hv=HelperView(request)
    hv.context['block_users']=block_users(request)
    return hv.render_template('admin_settings/settings_table.html')
    
def block_users(request):
    hv=HelperView(request)
    users = SysUser.objects.all().values()
    hv.context['users']=users
    return hv.get_template('admin_settings/settings_block_users.html')

def block_user_tables(request):
    hv=HelperView(request)
    bl=SettingsBusinessLogic()
    userid=request.POST.get('userid')
    
    tables=bl.get_user_tables()  
    
    hv.context['tables']=tables
    return hv.render_template('admin_settings/settings_block_user_tables.html')