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
from django.urls import path
from bixdata_app.views import alpha

urlpatterns = [
    path('', alpha.get_render_index, name='index'),
    path('index/', alpha.get_render_index, name='index'),
    path('loading/', alpha.get_render_loading, name='loading'),
    path('content_records/', alpha.get_content_records, name='content_records'),
    path('chart/', alpha.get_render_content_chart, name='charts_view'),
    path('block_records_table/', alpha.get_block_records_table, name='block_records_table'),
    path('block_records_gantt/', alpha.get_block_records_gantt, name='block_records_gantt'),
    path('block_records_kanban/', alpha.get_block_records_kanban, name='block_records_kanban'),
    path('block_records_calendar/', alpha.get_block_records_calendar, name='block_records_calendar'),
    path('block_records_chart/', alpha.get_block_records_chart, name='block_records_chart'),
    path('block_record/', alpha.get_block_record, name='block_record'),
    path('block_reload/', alpha.get_block_reload, name='block_reload'),
    path('block_record_card/', alpha.get_block_record_card, name='block_record_card'),
    path('test/', alpha.get_test, name='test'),
    path('temp/', alpha.get_temp, name='temp'),
    path('dashboard/', alpha.get_render_content_dashboard, name='dashboard'),
    path('record_card_copy/', alpha.get_record_card_copy, name='record_card_copy'),
    path('record_card_delete/', alpha.get_record_card_delete, name='record_card_delete'),
    path('record_card_permissions/', alpha.get_record_card_permissions, name='record_card_permissions'),
    path('record_card_pin/', alpha.get_record_card_pin, name='record_card_pin'),
    path('login/', alpha.get_render_login, name='login'),
    path('logout/', alpha.get_render_logout, name='logout'),
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


]
