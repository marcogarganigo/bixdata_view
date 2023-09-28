from django.contrib.sessions.models import Session
from bixdata_app.models import *

from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.core.mail import send_mail, BadHeaderError, EmailMessage
from django.http import HttpResponse
from django.template.loader import render_to_string
import requests
import json
import datetime
from django.contrib.auth.decorators import login_required
import time
from ...forms import LoginForm
from django.contrib.auth.decorators import user_passes_test
from django.contrib import messages
from django.db import connection, connections
from django.http import JsonResponse
from django.contrib.auth.models import Group, Permission, User, Group
from django_user_agents.utils import get_user_agent
#from bixdata_app.models import MyModel
from django import template
from bs4 import BeautifulSoup
from django.db.models import OuterRef, Subquery


class SettingsBusinessLogic:
    
    def __init__(self):
        self.test=None
    
    def get_user_tables(self):
        subquery = SysUserTableOrder.objects.filter(tableid=OuterRef('id')).values('tableorder')[:1]
        tables=dict()
        tables['selected'] = SysTable.objects.annotate(order=Subquery(subquery)).filter(order__isnull=False).order_by('workspace','order').values('id','description','workspace','order')  
        tables['notselected'] = SysTable.objects.annotate(order=Subquery(subquery)).filter(order__isnull=True).order_by('workspace','id').values('id','description','workspace','order') 
        return tables