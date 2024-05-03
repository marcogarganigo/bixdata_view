import locale
import tempfile
import uuid
import threading
from django.contrib.sessions.models import Session
import threading
from bixdata_app.models import *
from .businesslogic.helper_logic import *
from bixdata_app.models import *


import pyperclip
#from aiohttp.web_fileresponse import FileResponses
from django.core.files.storage import FileSystemStorage
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

import pdfkit

from ..forms import LoginForm
from django.contrib.auth.decorators import user_passes_test
from django.contrib import messages
from django.db import connection
from django.http import JsonResponse
from django.contrib.auth.models import Group, Permission, User, Group
from django_user_agents.utils import get_user_agent
import os
from django.conf import settings
from django.views.decorators.clickjacking import xframe_options_exempt
import subprocess
from .beta import *
from .helper_view import *
from htmldocx import HtmlToDocx
import csv
from functools import wraps
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.interval import IntervalTrigger
from apscheduler.jobstores.memory import MemoryJobStore
from apscheduler.executors.pool import ThreadPoolExecutor
from .businesslogic.bixdata_logic import *
from .businesslogic.settings_business_logic import *
from .businesslogic.models.record import *
from .businesslogic.models.table import *

bixdata_server = os.environ.get('BIXDATA_SERVER')

# Questa funzione ritorna la pagina index.html con le variabili riguardanti il menu, il nome utente, il ruolo, il tema e il contenuto
@firefox_check
@xframe_options_exempt
@login_required(login_url='/login/')
def index(request, content=''):
    hv=HelperView(request)
    
    sys_user = SysUser.objects.get(bixid=request.user.id)
    username = sys_user.username
    role = sys_user.description
    userid=sys_user.id
    
    menu_tables=BixdataLogic.get_menu_tables(userid)


    with connection.cursor() as cursor:
        cursor.execute(
            f"SELECT * FROM sys_user_dashboard WHERE userid = '{userid}'"
        )
        user_dashboards = dictfetchall(cursor)

    with connection.cursor() as cursor:
        cursor.execute(
            f"SELECT * FROM sys_dashboard"
        )
        dashboards = dictfetchall(cursor)


        active_dashboards = []

        for dashboard in dashboards:
            for user_dashboard in user_dashboards:
                if user_dashboard['dashboardid'] == dashboard['id']:
                    active_dashboards.append(dashboard)


    query = "SELECT tableid FROM sys_user_favorite_tables WHERE sys_user_id = '{}'".format(userid)

    with connection.cursor() as cursor:
        cursor.execute(
            query
        )
        favorite_tables = dictfetchall(cursor)

    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT * FROM sys_table"
        )
        tables = dictfetchall(cursor)


    if favorite_tables:
        i = 0
        for table in tables:
            if i < len(favorite_tables) and table['id'] == favorite_tables[i]['tableid']:
                favorite_tables[i]['description'] = table['description']
                i += 1

    query = "SELECT value FROM sys_user_settings WHERE setting = 'default_dashboard' AND userid = '{}'".format(userid)
    with connection.cursor() as cursor:
        cursor.execute(query)
        default_dashboard_result = cursor.fetchone()
        if default_dashboard_result:
            default_dashboard = int(default_dashboard_result[0].strip("'"))
        else:
            default_dashboard = None

    hv.context['menu_tables']=menu_tables
    hv.context['date']=datetime.datetime.now().strftime('%Y-%m-%d-%H:%M:%S')
    hv.context['username']=username
    hv.context['role']=role
    hv.context['theme']=get_user_setting(request, 'theme')
    hv.context['content']=content
    hv.context['layout_setting']=get_user_setting(request, 'record_open_layout')
    hv.context['active_dashboards'] = active_dashboards
    hv.context['favorite_tables'] = favorite_tables
    hv.context['default_dashboard'] = default_dashboard
    return hv.render_template('index_app.html')


@login_required(login_url='/login/')
def get_content_records(request):
    hv=HelperView(request)
    sbl=SettingsBusinessLogic()
    tableid = request.POST.get('tableid')
    us=sbl.get_usersettings(request.user.id)
    hv.context['records_table'] = ''
    hv.context['table'] = tableid.upper()
    hv.context['tableid'] = tableid
    hv.context['user_table_settings'] = get_user_table_settings(request.user.id, tableid)    
    hv.context['views']=list()
    hv.context['layout_setting'] = get_user_setting(request, 'record_open_layout')
    hv.context['active_panel_setting'] = us.active_panel
    hv.context['selected_view']=hv.context['user_table_settings']['default_viewid'] 

    t=Table(tableid=tableid,userid=1)
    t.context='search_fields'
    filter_fields=t.get_fields()
  
    return hv.render_template('content/records_app.html')


@login_required(login_url='/login/')
def get_records_table_render(request):
    tableid = request.POST.get('tableid')
    master_tableid = request.POST.get('master_tableid')
    master_recordid = request.POST.get('master_recordid')
    searchTerm = request.POST.get('searchTerm')
    viewid = request.POST.get('viewid')
    filters=request.POST.get('filters')
    filters_dict=dict()
    order_field = request.POST.get('order_field')
    order = request.POST.get('order')
    currentpage = request.POST.get('currentpage')
    if (currentpage == ''):
        currentpage = 1
    render = get_records_table(request, tableid, master_tableid, master_recordid, searchTerm, viewid, currentpage,order_field, order, filters)
    return HttpResponse(render)


@login_required(login_url='/login/')
def get_records_table(request, tableid, master_tableid='', master_recordid='', searchTerm='', viewid='', currentpage=1,order_field='', order='', filters=dict()):
    userid = get_userid(request.user.id)
    table_type = 'standard'
    table_height = '100%'

    if master_tableid == '':
        master_tableid = None

    if master_recordid == '':
        master_recordid = None

    if master_tableid:
        table_height = '500px'
        table_type = 'linked'

    post = {
        'tableid': tableid,
        'searchTerm': searchTerm,
        'viewid': viewid,
        'currentpage': currentpage,
        'order_field': order_field,
        'order': order,
        'master_tableid': master_tableid,
        'master_recordid': master_recordid,
        'userid': userid,
        'filters':filters
    }
    response = requests.post(f"{bixdata_server}bixdata/index.php/rest_controller/get_records", data=post)
    response_dict = json.loads(response.text)
    columns = response_dict['columns']
    records = response_dict['records']
    reports = response_dict['reports']
    other_values = dict()

    if order_field == '' or order_field == None:
        order_field = columns[3]['desc']
        order = 'asc'

    if order == 'asc':
        icon = 'mdi mdi-arrow-down-thin'
    else:
        icon = 'mdi mdi-arrow-up-thin'

    context = {
        'records': records,
        'reports': reports,
        'columns': columns,
        'tableid': tableid,
        'table_height': table_height,
        'table_type': table_type,
        'other_values': other_values,
        'currentpage': currentpage,
        'order_field': order_field,
        'order': order,
        'icon': icon
    }

    with connection.cursor() as cursor:
        cursor.execute(
            f"SELECT column_width FROM sys_user_column_width WHERE tableid = %s AND userid = %s",
            [tableid, get_userid(request.user.id)]
        )
        column_width = cursor.fetchone()

        if column_width:
            column_width = column_width[0]
            context['column_width'] = column_width

    for records_index, record in enumerate(records):
        for record_index, value in enumerate(record):
            record[record_index] = dict()
            record[record_index]['value'] = value
            record[record_index]['code'] = value
            record[record_index]['fieldtype'] = columns[record_index]['fieldtypeid'];
            record[record_index]['fieldtypeweb'] = columns[record_index]['fieldtypewebid'];
            if record[record_index]['fieldtype'] == 'linked':
                if isinstance(value, str):
                    value = value.split('|:|')
                    if (len(value) > 2):
                        record[record_index]['value'] = value[0]
                        record[record_index]['link_recordid'] = value[1]
                        record[record_index]['link_tableid'] = value[2]
                        record[record_index]['fieldtype'] = 'linked'
            if record[record_index]['fieldtype'] == 'Utente':
                code = record[record_index]['code']
                code = code.replace(' ', '.')
                code = code.lower()
                record[record_index]['code'] = code
            if record[record_index]['fieldtype'] == 'Numero':
                num_str = record[record_index]['value']

                if num_str:
                    # Split the number into the integer and decimal parts
                    if '.' in num_str:
                        integer_part, decimal_part = num_str.split('.')
                    else:
                        integer_part, decimal_part = num_str, ""

                    if decimal_part == '':
                        decimal_part = '00'

                    # Add thousands separators (period) to the integer part
                    integer_part = format(int(integer_part), ',').replace(',', '.')
                    formatted_num = f"{integer_part},{decimal_part}"

                    record[record_index]['value'] = formatted_num

            if record[record_index]['value'] == 'Validazionetecnica':
                record[record_index]['fieldtype'] = 'lookup'
                record[record_index]['fieldbackground'] = 'green'
            if record[record_index]['value'] == 'Controllosolvibilita':
                record[record_index]['fieldtype'] = 'lookup'
                record[record_index]['fieldbackground'] = 'red'
            if record[record_index]['value'] == 'Chiusovinto':
                record[record_index]['fieldtype'] = 'lookup'
                record[record_index]['fieldbackground'] = 'blue'

        records[records_index] = record

    records_table = bix_render_to_string('block/records/records_table_app.html', context, request)
    return records_table


@login_required(login_url='/login/')
def get_record_card_app(request):
    tableid = request.POST.get('tableid')
    recordid = request.POST.get('recordid')
    master_tableid = request.POST.get('master_tableid')
    master_recordid = request.POST.get('master_recordid')
    userid = request.user.id
    return HttpResponse(get_block_record_card(request, tableid, recordid, userid, master_tableid, master_recordid))


# Questa funzione serve per creare la record card e ritorna la card come stringa
def get_block_record_card(request, tableid, recordid, userid, master_tableid='', master_recordid=''):
    context = dict()
    context['block_record_badge'] = get_block_record_badge(tableid, recordid)
    context['block_record_linked'] = get_block_record_linked(tableid, recordid)
    context['block_record_fields'] = ""
    context['recordid'] = recordid
    context['tableid'] = tableid
    context['master_tableid']=master_tableid
    context['master_recordid']=master_recordid
    context['layout_setting'] = get_user_setting(request, 'record_open_layout')
    if tableid == 'ticket':
        with connection.cursor() as cursor:
            cursor.execute(f"SELECT freshdeskid FROM user_ticket WHERE recordid_={recordid}")
            freshdeskid = cursor.fetchone()[0]
            context['freshdeskid'] = freshdeskid
    if tableid == 'deal':
        deal_record=Record(tableid='deal',recordid=recordid)
        context['dealstatus']=deal_record.fields['dealstatus']
    context['userid'] = userid
    context['user_table_settings'] = get_user_table_settings(userid, tableid)
    # TODO: recuperare i dati dal table settings generico
    context['recordtab']='fields'
    if tableid == 'deal':
        context['recordtab']='linked'
    # returned = user_agent(request, 'block/record/record_card.html', 'block/record/record_card_mobile.html', context)
    return render_to_string('block/record/record_card_app.html', context)


# Questa funzione serve per creare il badge
def get_block_record_badge(tableid, recordid):
    print(f'get_block_record_badge {tableid} {recordid}')
    context = dict()

    post = {
        'tableid': tableid,
        'recordid': recordid,
    }
    # response = requests.post("http://10.0.0.133:8822/bixdata/index.php/rest_controller/get_fissi", data=post)
    # response_dict = json.loads(response.text)
    sql = f"SELECT sys_field.* FROM sys_field join sys_user_order on sys_field.fieldid=sys_user_order.fieldid WHERE sys_user_order.userid=1 AND sys_user_order.tableid='{tableid}' AND typePreference='campiFissi' ORDER BY fieldorder asc"

    fields = db_query_sql(sql)
    values = db_get_row(f"user_{tableid}", "*", f"recordid_='{recordid}'")
    context_fields = dict()
    for field in fields:
        fieldid = field['fieldid']
        field['value'] = values[fieldid]
        context_fields[fieldid] = field

    context['fields'] = context_fields

    records_table = ""
    block_record_badge = ''

    if tableid == 'company':
        sql = f"SELECT DISTINCT type FROM user_servicecontract WHERE recordidcompany_='{recordid}' AND STATUS='In Progress'"
        context_fields['services'] = db_query_sql(sql)
        context['fields'] = context_fields
        block_record_badge = render_to_string('block/record/custom/record_badge_company.html', context)
    elif tableid == 'deal':
        deal_record = Record('deal', recordid)
        company_record = Record(tableid='company', recordid=deal_record.fields['recordidcompany_'])
        deal_record.fields['companyname'] = company_record.fields['companyname']
        context['fields'] = deal_record.fields
        block_record_badge = render_to_string('block/record/custom/record_badge_deal.html', context)
    else:
        block_record_badge = render_to_string('block/record/record_badge.html', context)
    return block_record_badge


def get_block_record_linked(tableid, recordid):
    context = dict()

    rows = db_query_sql(
        f"SELECT sys_table_link.*,typepreference,sys_user_order.ID FROM sys_table_link JOIN sys_user_order ON sys_table_link.tableid=sys_user_order.tableid AND sys_table_link.tablelinkid=sys_user_order.fieldid  WHERE sys_table_link.tableid = '{tableid}' AND typepreference='keylabel'")

    linked_tables = list()
    for row in rows:
        linked_table = dict()
        linked_tableid = row['tablelinkid']
        table_name = 'test'
        linked_table['table_name'] = db_get_value("sys_table", "description", f"id='{linked_tableid}'")
        table_count = db_get_count(f"user_{linked_tableid}", f"recordid{tableid}_='{recordid}'")
        linked_table['table_count'] = table_count
        linked_table['tableid'] = linked_tableid
        linked_tables.append(linked_table)

    context['linked_tables'] = linked_tables
    context['tableid'] = tableid
    context['recordid'] = recordid

    record_linked_labels = render_to_string('block/record/record_linked.html', context)
    return record_linked_labels

@login_required(login_url='/login/s')
def get_block_record_fields_app(request, prefilled_fields=dict()):
    context = dict()
    http_response = request.POST.get('http_response')
    tableid = request.POST.get('tableid')
    recordid = request.POST.get('recordid')
    ticketid = request.POST.get('ticketid')
    recordid_ticket = request.POST.get('recordid_ticket')
    master_tableid = request.POST.get('master_tableid')
    master_recordid = request.POST.get('master_recordid')
    contextfunction = request.POST.get('contextfunction')
    contextreference = request.POST.get('contextreference')
    # creator = request.POST.get('creator')

    row = SysUser.objects.filter(bixid=request.user.id).values('id')

    if row:
        userid = row[0]
        userid = userid['id']
        context['userid'] = userid

    record = Record(tableid=tableid, recordid=recordid, userid=userid)
    record.master_tableid = master_tableid
    record.master_recordid = master_recordid
    record.context = contextfunction
    fields = record.get_fields()

    context['record_fields_labels'] = fields
    context['contextfunction'] = contextfunction
    context['contextreference'] = contextreference
    context['tableid'] = tableid
    context['recordid'] = recordid
    context['master_tableid'] = master_tableid
    context['master_recordid'] = master_recordid

    bixuserid = get_userid(request.user.id)

    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT value FROM sys_user_settings WHERE setting = 'record_open_layout' AND userid = %s",
            [bixuserid]
        )
        user_setting = cursor.fetchone()
        user_setting = user_setting[0]

        context['user_setting'] = user_setting

    if tableid == 'timesheet':
        context['timesheet'] = uuid.uuid4()
        if contextfunction != 'insert':
            timesheet_record = Record(tableid='timesheet', recordid=recordid)

            if timesheet_record.fields['validated'] == 'Si':
                context['edit_block'] = True
            else:
                context['edit_block'] = False

            if userid in [53, 2, 47, 50, 3]:
                context['edit_block'] = False
        else:
            context['edit_block'] = False

        context['block_record_fields_timesheet'] = render_to_string('block/record/record_fields_app.html', context,
                                                                    request=request)
        context['block_record_fields'] = render_to_string('block/record/custom/record_fields_timesheet_app.html', context,
                                                          request=request)
        block_record_fields_container = render_to_string('block/record/record_fields_container_app.html', context,
                                                         request=request)
    else:
        context['block_record_fields'] = render_to_string('block/record/record_fields_app.html', context, request=request)
        block_record_fields_container = render_to_string('block/record/record_fields_container_app.html', context,
                                                         request=request)

    if (http_response):
        return HttpResponse(block_record_fields_container)
    else:
        return block_record_fields_container





