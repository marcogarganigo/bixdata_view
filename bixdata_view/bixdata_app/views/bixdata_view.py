import locale
import tempfile
import uuid
import threading
from django.contrib.sessions.models import Session
import threading
from bixdata_app.models import *
from .businesslogic.helper_business_logic import *
from bixdata_app.models import *


import pyperclip
from aiohttp.web_fileresponse import FileResponse
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
from .businesslogic.bixdata_business_logic import *
from .businesslogic.settings_business_logic import *

bixdata_server = os.environ.get('BIXDATA_SERVER')

# Questa funzione ritorna la pagina index.html con le variabili riguardanti il menu, il nome utente, il ruolo, il tema e il contenuto
@firefox_check
@xframe_options_exempt
@login_required(login_url='/login/')
def index(request, content=''):
    hv=HelperView(request)
    bl=BixdataBusinessLogic()
    
    sys_user = SysUser.objects.get(bixid=request.user.id)
    username = sys_user.username
    role = sys_user.description
    userid=sys_user.id
    
    menu_tables=bl.get_menu_tables(userid)
    response = requests.get(f"{bixdata_server}bixdata/index.php/rest_controller/get_tables_menu")
    menu_list = json.loads(response.text)

    

    hv.context['menu_tables']=menu_tables
    hv.context['menu_list']=menu_list
    hv.context['date']=datetime.datetime.now().strftime('%Y-%m-%d-%H:%M:%S')
    hv.context['username']=username
    hv.context['role']=role
    hv.context['theme']=get_user_setting(request, 'theme')
    hv.context['content']=content
    hv.context['layout_setting']=get_user_setting(request, 'record_open_layout')
    return hv.render_template('index.html')


# Questa funzione ritorna la pagina records.html ovvero la tabella, la vista della tabella e le impostazioni rigurdanti la tabella
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
    hv.context['views']=list(SysView.objects.filter(userid=1).filter(tableid=tableid).values())
    hv.context['layout_setting'] = us.record_open_layout
    hv.context['active_panel_setting'] = us.active_panel

    #  search fields
    search_fields = dict()
    with connection.cursor() as cursor:
        cursor.execute(
            f"SELECT f.* FROM sys_user_table_search_field AS s join sys_field as f on s.tableid=f.tableid and s.fieldid=f.fieldid  WHERE s.tableid='{tableid}'"
        )
        result = dictfetchall(cursor)
        if result:
            search_fields = result
    for search_field_key, search_field in enumerate(search_fields):
        context_search_field = dict()
        context_search_field['search_field'] = search_field
        search_fields[search_field_key]['component'] = render_to_string('components/search_field.html',
                                                                        context_search_field, request)

    hv.context['search_fields'] = search_fields
    return hv.render_template('content/records.html')



# Questa funzione prende in post tutte le variabili e ritorna i records della tabella richiesta
@login_required(login_url='/login/')
def get_records_table_render(request):
    tableid = request.POST.get('tableid')
    master_tableid = request.POST.get('master_tableid')
    master_recordid = request.POST.get('master_recordid')
    searchTerm = request.POST.get('searchTerm')
    viewid = request.POST.get('viewid')
    order_field = request.POST.get('order_field')
    order = request.POST.get('order')
    currentpage = request.POST.get('currentpage')
    if (currentpage == ''):
        currentpage = 1
    render = get_records_table(request, tableid, master_tableid, master_recordid, searchTerm, viewid, currentpage,order_field, order)
    return HttpResponse(render)


# Questa funzione ritorna i record delle tabelle collegate
def get_records_linked(request):
    tableid = request.POST.get('tableid')
    master_tableid = request.POST.get('master_tableid')
    master_recordid = request.POST.get('master_recordid')
    records_table = get_records_table(request, tableid, master_tableid, master_recordid)
    return HttpResponse(records_table)

# Questa funzione prende tutti i record della tabella richiesta e li ritorna
@login_required(login_url='/login/')
def get_records_table(request, tableid, master_tableid='', master_recordid='', searchTerm='', viewid='', currentpage=1,order_field='', order=''):
    userid = get_userid(request.user.id)
    table_type = 'standard'
    table_height = '100%'

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
        'userid': userid
    }
    response = requests.post(
        f"{bixdata_server}bixdata/index.php/rest_controller/get_records", data=post)
    response_dict = json.loads(response.text)
    columns = response_dict['columns']
    records = response_dict['records']
    reports = response_dict['reports']
    other_values = dict()

    if order_field == '':
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

    records_table = bix_render_to_string('block/records/records_table.html', context, request)
    return records_table