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

