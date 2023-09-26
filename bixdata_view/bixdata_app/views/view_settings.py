from .alpha import *
from .view_helper import *
from django.db.models import OuterRef, Subquery

@login_required(login_url='/login/')
def settings_table(request):
    vh=ViewHelper(request)
    vh.context['block_users_list']=block_users(request)
    return vh.render_template('admin_settings/settings_table.html')
    
def block_users(request):
    vh=ViewHelper(request)
    users = SysUser.objects.all().values()
    vh.context['users']=users
    return vh.get_template('admin_settings/settings_block_users.html')

def block_user_tables(request):
    vh=ViewHelper(request)
    userid=request.POST.get('userid')
    
    subquery = SysUserTableOrder.objects.filter(tableid=OuterRef('id')).values('tableorder')[:1]
    tables = SysTable.objects.annotate(qwe=Subquery(subquery)).filter(qwe__isnull=False).values('id','description','qwe')    
    
    vh.context['tables']=tables
    return vh.render_template('admin_settings/settings_block_user_tables.html')