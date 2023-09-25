from .alpha import *
from .view_helper import *

@login_required(login_url='/login/')
def settings_table(request):
    vh=ViewHelper(request)
    vh.context['users_list']=block_users_list(request)
    return vh.render_template('admin_settings/settings_table.html')
    
def block_users_list(request):
    vh=ViewHelper(request)
    users = SysUser.objects.all().values()
    vh.context['users']=users
    return vh.get_template('admin_settings/settings_users_list.html')

def user_tables_list(request):
    vh=ViewHelper(request)
    return vh.render_template('admin_settings/user_tables_list.html')