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
from django import template


def user_agent(request, page, mobilepage, context={}):
    user_agent = get_user_agent(request)
    if user_agent.is_mobile:
        return render(request, mobilepage, context)
    else:
        return render(request, page, context)


def bix_render_to_string(template_path, context, request):
    context['date'] = datetime.datetime.now().strftime('%Y-%m-%d-%H:%M:%S')
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
        # Get settings for superuser
        superuser_id = 1

        with connection.cursor() as cursor:
            cursor.execute("SELECT id FROM sys_user WHERE bixid = %s", [request.user.id])
            row = cursor.fetchone()

            userid = row[0]

        with connection.cursor() as cursor:
            cursor.execute("SELECT setting, value FROM v_sys_user_settings WHERE bixid = %s", [superuser_id])
            admin_rows = cursor.fetchall()
            admin_settings_list = [{'setting': row[0], 'value': row[1]} for row in admin_rows]

            settings_count = len(admin_rows)

        with connection.cursor() as cursor:
            cursor.execute("SELECT setting, value FROM v_sys_user_settings WHERE bixid = %s", [request.user.id])
            user_rows = cursor.fetchall()

        if len(user_rows) == settings_count:
            settings_list = [{'setting': row[0], 'value': row[1]} for row in user_rows]
            return settings_list
        else:
            settings_list = admin_settings_list.copy()
            user_settings = {row[0]: row[1] for row in user_rows}
            missing_settings = [setting for setting in admin_settings_list if setting['setting'] not in user_settings]

            with connection.cursor() as cursor:
                for setting in missing_settings:
                    cursor.execute("INSERT INTO sys_user_settings (userid, setting, value) VALUES (%s, %s, %s)",
                                   [userid, setting['setting'], setting['value']])

            settings_list += missing_settings
            return settings_list




def get_userid(django_userid):
    userid = 0
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


def get_user_table_settings(bixid, tableid):
    returned_settings = dict()
    settings = list()
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
        returned_settings[setting['settingid']] = setting['value']

    returned_settings['default_viewid'] = int(returned_settings['default_viewid'])
    return returned_settings


def send_email(request=None, emails=None, subject=None, message=None,html_message=None):
    send_mail(
        subject=subject,
        message=message,
        from_email='bixdata@sender.swissbix.ch',
        recipient_list=emails,
        fail_silently=False,
        html_message=html_message
    )
    return True


def db_query_sql(sql):
    rows = dict()
    with connection.cursor() as cursor:
        cursor.execute(sql)
        rows = dictfetchall(cursor)
    return rows


def db_get(table, columns, condition, order='', limit=''):
    sql = f"SELECT {columns} FROM {table} WHERE {condition}"
    rows = db_query_sql(sql)
    return rows


def db_get_row(table, columns, condition, order=''):
    sql = f"SELECT {columns} FROM {table} WHERE {condition} LIMIT 1"
    rows = db_query_sql(sql)
    if rows:
        return rows[0]
    else:
        return None


def db_get_value(table, column, condition, order=''):
    sql = f"SELECT {column} FROM {table} WHERE {condition} LIMIT 1"
    rows = db_query_sql(sql)
    if rows:
        return rows[0][column]
    else:
        return None


def db_get_count(table, condition, order=''):
    sql = f"SELECT count(*) as counter FROM {table} WHERE {condition}"
    rows = db_query_sql(sql)
    if rows:
        return rows[0]['counter']
    else:
        return None


def generate_recordid(tableid):
    tableid = 'user_task'
    sql = f"SELECT recordid_ FROM {tableid} WHERE recordid_ NOT LIKE '1%' ORDER BY recordid_ DESC LIMIT 1"
    rows = db_query_sql(sql)
    recordid = rows[0]['recordid_']
    recordid = int(recordid) + 1
    recordid = str(recordid).zfill(32)

    return recordid

        