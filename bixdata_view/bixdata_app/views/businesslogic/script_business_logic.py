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
from .record_helper import *
from .records_helper import *
 


class ScriptBusinessLogic:
    
    def __init__(self):
        self.test=None
    
    def update_deals(self):
        return_value=False
        RecordsH=RecordsHelper('deal')
        RecordH=RecordHelper('deal')
        conditions=list()
        conditions.append("status='Closed'")
        records= RecordsH.get_records(conditions)
        for record in records:
            return_value=True
        return return_value
   

