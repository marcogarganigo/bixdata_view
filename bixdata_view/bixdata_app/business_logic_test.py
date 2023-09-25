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


class BusinessLogicTest:
    
    def __init__(self):
        self.test=None
    
    def bl_test(self,userid):
        ## recuperare un record e il record collegato e trasformarlo da object a dict
        #e = SysUserSettings.objects.get(id=3)
        #b = e.userid
        #return_value = b.__dict__
        
        # Hits the database.
        e = SysUserSettings.objects.select_related("userid").get(id=3)
        b = e.userid
        return_value = b.__dict__

        #my_queryset = SysUserSettings.objects.select_related('userid').all()
        #related_settings = my_queryset.user
        #return_value = list(my_queryset.values())
        #return_value = b.values().first()
        
        
        return return_value
    
