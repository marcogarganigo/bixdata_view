import tempfile
import uuid
import threading
from django.contrib.sessions.models import Session
import threading
from bixdata_app.models import *
from .businesslogic.test_business_logic import *


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
from htmldocx import HtmlToDocx
import csv
from functools import wraps
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.interval import IntervalTrigger
from apscheduler.jobstores.memory import MemoryJobStore
from apscheduler.executors.pool import ThreadPoolExecutor
from .helper_view import *


bixdata_server = os.environ.get('BIXDATA_SERVER')

def test(request):
    num = 1
    return render(request, 'test/test_table.html', {'num': num})

@login_required(login_url='/login/')
def test_content(request):
    vh=ViewHelper(request)
    bl= TestBusinessLogic()
    
    
    content_page = request.POST.get('content_page')
    bl_returned=None
    vh.context['bl_returned']=bl.bl_test(1)
    return vh.render_template('test/test_content.html')

# Questa funzione è per il testing delle query
def get_test_query(request, name=None):
    return render(request, 'other/test_query.html')


def get_query_to_test(request):
    query = request.POST.get('query')
    print(query)
    query = 'test_' + query

    if query in globals() and callable(globals()[query]):
        function = globals()[query]
    return HttpResponse(function(request))


def test_leftjoin(request):
    hv=HelperView(request)
    bl=TestBusinessLogic()
    tables=bl.test_leftjoin()
    hv.context['tables']=tables
    return hv.render_template('admin_settings/settings_block_user_tables.html')


def test_query1(request):
    return HttpResponse('contenuto query 2')