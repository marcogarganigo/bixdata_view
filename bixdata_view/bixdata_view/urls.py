"""bixdata_view URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

from bixdata_app.views import alpha
from bixdata_app.views import beta

urlpatterns = [
    path('', alpha.get_render_index, name='index'),
    path('index/', alpha.get_render_index, name='index'),
    path('loading/', alpha.get_render_loading, name='loading'),
    path('content_records/', alpha.get_content_records, name='content_records'),
    path('chart/', alpha.get_render_content_chart, name='charts_view'),
    path('block_records_table/', alpha.get_records_table_render, name='block_records_table'),
    path('block_records_gantt/', alpha.get_block_records_gantt, name='block_records_gantt'),
    path('block_records_kanban/', alpha.get_block_records_kanban, name='block_records_kanban'),
    path('block_records_calendar/', alpha.get_block_records_calendar, name='block_records_calendar'),
    path('block_records_chart/', alpha.get_block_records_chart, name='block_records_chart'),
    path('block_record/', alpha.get_block_record, name='block_record'),
    path('block_reload/', alpha.get_block_reload, name='block_reload'),
    path('block_record_card/', alpha.request_block_record_card, name='block_record_card'),
    path('test/', alpha.get_test, name='test'),
    path('temp/', alpha.get_temp, name='temp'),
    path('dashboard/', alpha.get_render_content_dashboard, name='dashboard'),
    path('record_card_copy/', alpha.record_card_copy, name='record_card_copy'),
    path('record_card_duplicate/', alpha.record_card_duplicate, name='record_card_duplicate'),
    path('record_card_delete/', alpha.get_record_card_delete, name='record_card_delete'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    # path('login/', alpha.get_render_login, name='login'),
    # path('logout/', alpha.get_render_logout, name='logout'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('test_query/', alpha.get_test_query, name='test_query'),
    path('test_query2/', alpha.get_test_query2, name='test_query2'),
    path('get_full_data/', alpha.get_full_data, name='get_full_data'),
    path('get_full_data2/', alpha.get_full_data2, name='get_full_data2'),
    path('get_linked/', alpha.get_linked, name='get_linked'),
    path('get_record_fields/', alpha.get_block_record_fields, name='get_record_fields'),
    path('admin/', admin.site.urls),
    path('save_record_fields/', alpha.save_record_fields, name='save_record_fields'),
    path('get_chart3/', alpha.get_chart3, name='get_chart3'),
    path('test_autocomplete/', alpha.get_test_autocomplete, name='test_autocomplete'),
    path('autocomplete/', alpha.get_autocomplete_data, name='get_autocomplete_data'),
    path('get_chart4/', alpha.get_chart4, name='get_chart4'),
    path('pagination/', alpha.pagination, name='pagination'),
    path('testcalendar/', alpha.get_test_calendar, name='testcalendar'),
    path('get_records_linked/', alpha.get_records_linked, name='get_records_linked'),
    path('get_chart/', alpha.get_chart, name='get_chart'),
    # path('accounts/', include('django.contrib.auth.urls')),
    # Password reset URLs
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('get_settings/', alpha.get_settings, name='get_settings'),
    path('get_user_setting/', beta.get_user_setting, name='get_user_setting'),
    path('under_construction/', alpha.get_under_construction, name='under_construction'),
    path('support/', alpha.support, name='support'),
    path('save_settings/', alpha.save_settings, name='save_settings'),
    path('get_account/', alpha.get_account, name='get_account'),
    path('update_profile_pic/', alpha.update_profile_pic, name='update_profile_pic'),
    # path('get_url/', alpha.get_url, name='get_url'),
    path('accounts/password-reset/',
         auth_views.PasswordResetView.as_view(html_email_template_name='registration/password_reset_email.html'),
         name='password_reset'),
    path('get_badge/', alpha.get_badge, name='get_badge'),
    path('get_timesheet_serviceassets/', alpha.get_timesheet_serviceassets, name='get_timesheet_serviceassets'),
    path('get_block_record_badge/', alpha.request_block_record_badge, kwargs={'http_response': True},name='get_block_record_badge'),
    path('get_bixdata_updates/', alpha.get_bixdata_updates, name='get_bixdata_updates'),
    path('new_update/', alpha.new_update, name='new_update'),
    path('admin_page/', alpha.admin_page, name='admin_page'),
    path('save_chart_settings/', alpha.save_chart_settings, name='save_chart_settings'),
    path('get_record_path/<str:tableid>/<str:recordid>/', alpha.get_record_path, name='get_record_path'),
    path('new_chart_block/', alpha.new_chart_block, name='new_chart_block'),
    path('stampa_timesheet/', alpha.stampa_timesheet, name='stampa_timesheet'),
    path('stampa_servicecontract/', alpha.stampa_servicecontract, name='stampa_servicecontract'),
    path('new_ticket_timesheet/<str:ticket>/', alpha.new_ticket_timesheet, name='new_ticket_timesheet'),
    path('rinnova_contratto/', alpha.rinnova_contratto, name='rinnova_contratto'),
    path('sort_records/', alpha.sort_records, name='sort_records'),
    path('export_excel/', alpha.export_excel, name='export_excel'),
    path('stampa_servicecontract_test/', alpha.stampa_servicecontract_test, name='stampa_servicecontract_test'),
    path('get_records_grouped/', alpha.get_records_grouped, name='get_records_grouped'),
    path('send_active_task/', alpha.send_active_task, name='send_active_task'),
    path('send_unique_active_task/', alpha.send_unique_active_task, name='send_unique_active_task'),
    path('update_task_status/', alpha.update_task_status, name='update_task_status'),
    path('generate_recordid/', beta.generate_recordid, name='generate_recordid'),
    path('update_task_status/', alpha.update_task_status, name='update_task_status'),
    path('validate_timesheet/', alpha.validate_timesheet, name='validate_timesheet'),
    path('scheduler/', alpha.scheduler, name='scheduler'),
    path('save_scheduler_settings/', alpha.save_scheduler_settings, name='save_scheduler_settings'),
    path('run_tasks/', alpha.run_tasks, name='run_tasks'),
    path('test_gridstack/', alpha.test_gridstack, name='test_gridstack'),
    path('save_block_order/', alpha.save_block_order, name='save_block_order'),
    path('new_block/', alpha.new_block, name='new_block'),
    path('remove_block/', alpha.remove_block, name='remove_block'),
]
