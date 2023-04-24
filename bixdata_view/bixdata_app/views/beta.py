from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.template.loader import render_to_string
import requests
import json
import datetime
from django.contrib.auth.decorators import login_required
import time
from ..forms import LoginForm
from django.contrib.auth.decorators import user_passes_test
from django.contrib import messages
from django.db import connection
from django.http import JsonResponse
from django.contrib.auth.models import Group, Permission, User, Group
from django_user_agents.utils import get_user_agent
from bixdata_app.models import MyModel
from .alpha import *


def user_agent(request, page, mobilepage, context={}):
    user_agent = get_user_agent(request)
    if user_agent.is_mobile:
        return render(request, mobilepage, context)
    else:
        return render(request, page, context)

def bix_render_to_string(template_path,context,request):
    context['date']=datetime.datetime.now().strftime('%Y-%m-%d-%H:%M:%S')
    return render_to_string(template_path, context, request)
# from .models import Login
def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]


def get_user_setting_list(request):
    if request.user.is_authenticated:
        # settings superuser
        id = 1
        with connection.cursor() as cursor:
            cursor.execute("SELECT setting, value FROM v_sys_user_settings WHERE bixid = %s", [id])
            rows = cursor.fetchall()
            settings_list = []

            for row in rows:
                settings_list.append({'setting': row[0], 'value': row[1]})

            return settings_list


def get_userid(django_userid):
    userid=0
    with connection.cursor() as cursor:
        cursor.execute("SELECT id FROM sys_user WHERE bixid = %s", [django_userid])
        row = cursor.fetchone()
        if row:
            userid = row[0]
    return userid        

def get_user_setting(request, setting):
    # settings superuser
    returned_value = ''
    id = request.user.id
    with connection.cursor() as cursor:
        cursor.execute("SELECT value FROM v_sys_user_settings WHERE bixid = %s AND setting = %s", [id, setting])
        result = cursor.fetchone()
        if result:
            returned_value = result[0]
        else:
            with connection.cursor() as cursor:
                cursor.execute("SELECT value FROM v_sys_user_settings WHERE bixid = %s AND setting = %s", [1, setting])
                result = cursor.fetchone()
                if result:
                    returned_value = result[0]

    return returned_value

def get_user_table_settings(bixid,tableid):
    returned_settings = dict()
    settings=list()
    with connection.cursor() as cursor:
        cursor.execute(f"SELECT * FROM v_sys_user_table_settings WHERE bixid = {bixid} and tableid= '{tableid}'")
        result = dictfetchall(cursor)
        if result:
            settings = result
        else:
            with connection.cursor() as cursor:
                cursor.execute(f"SELECT * FROM v_sys_user_table_settings WHERE bixid = 1 and tableid='{tableid}' ")
                result = dictfetchall(cursor)
                if result:
                    settings = result

    for setting in settings:
        returned_settings[setting['settingid']]=setting['value']

        
    return returned_settings


def send_email(request, email, subject, message):
    send_mail(
        subject,
        message,
        'bixdata@sender.swissbix.ch',
        email,
        fail_silently=False,
    )
    return True

def db_query_sql(sql):
    rows=dict()
    with connection.cursor() as cursor:
        cursor.execute(sql)
        rows = dictfetchall(cursor)
    return rows

def db_get(table,columns,condition,order='',limit=''): 
    sql=f"SELECT {columns} FROM {table} WHERE {condition}"
    rows= db_query_sql(sql)
    return rows

def db_get_row(table,columns,condition,order=''):
    sql=f"SELECT {columns} FROM {table} WHERE {condition} LIMIT 1"
    rows= db_query_sql(sql)
    if rows:
        return rows[0]
    else:
        return None
    
def db_get_value(table,column,condition,order=''):
    sql=f"SELECT {column} FROM {table} WHERE {condition} LIMIT 1"
    rows= db_query_sql(sql)
    if rows:
        return rows[0][column]
    else:
        return None

def db_get_count(table,condition,order=''):
    sql=f"SELECT count(*) as counter FROM {table} WHERE {condition}"
    rows= db_query_sql(sql)
    if rows:
        return rows[0]['counter']
    else:
        return None