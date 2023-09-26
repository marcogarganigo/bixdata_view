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
from .forms import LoginForm
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


class BusinessLogicTest:
    
    def __init__(self):
        self.test=None
    
    def bl_test(self,userid):
        ## recuperare un record e il record collegato e trasformarlo da object a dict
        e = SysUserSettings.objects.get(id=3)
        b = e.userid
        #return_value = b.__dict__
        
        ## recuperare un record collegato e trasformarlo in dct usando la select_related
        e = SysUserSettings.objects.select_related("userid").get(id=3)
        b = e.userid
        #return_value = b.__dict__

        ## recuperare una query set di tutte le impostazioni 
        my_queryset = SysUserSettings.objects.all()
        #return_value = list(my_queryset.values())
        
        ## recuperare una query set di tutte le impostazioni filtrate per tipo
        my_queryset = SysUserSettings.objects.filter(setting='theme')
        return_value = list(my_queryset.values())
        
        ## recuperare una query set di tutte le impostazioni filtrate per utente nella tabella collegata
        my_queryset = SysUserSettings.objects.filter(userid__username='superuser')
        #return_value = list(my_queryset.values())
        
        ## recuperare una query set di impostazioni e impostazioni utente in join
        my_queryset=SysUserSettings.objects.select_related("userid").all()
        return_value = list(my_queryset.values())
        
        return return_value
    
    def test_leftjoin(self):
        subquery = SysUserTableOrder.objects.filter(tableid=OuterRef('id')).values('tableorder')[:1]
        # il filtro is null lo metto o meno se voglio filtrare sui risultati presenti della tabella relativa
        tables = SysTable.objects.annotate(qwe=Subquery(subquery)).filter(qwe__isnull=False).values('id','description','qwe')  
        return tables  
    
