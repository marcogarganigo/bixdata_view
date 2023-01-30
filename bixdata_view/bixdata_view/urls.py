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
from bixdata_app import views

urlpatterns = [
    path('', views.get_render_index, name='index'),
    path('index/', views.get_render_index, name='index'),
    path('loading/', views.get_render_loading, name='loading'),
    path('content_records/', views.get_content_records, name='content_records'),
    path('charts/', views.get_render_content_charts, name='charts_view'),
    path('block_records_table/', views.get_block_records_table, name='block_records_table'),
    path('block_records_gantt/', views.get_block_records_gantt, name='block_records_gantt'),
    path('block_records_kanban/', views.get_block_records_kanban, name='block_records_kanban'),
    path('block_records_calendar/', views.get_block_records_calendar, name='block_records_calendar'),
    path('block_record/', views.get_block_record, name='block_record'),
    path('block_record_card/', views.get_block_record_card, name='block_record_card'),
    path('test/', views.get_test, name='test'),
]
