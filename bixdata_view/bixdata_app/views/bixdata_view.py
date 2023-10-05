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
