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
    path('records/', views.get_render_content_records, name='records_view'),
    path('charts/', views.get_render_content_charts, name='charts_view'),
]
