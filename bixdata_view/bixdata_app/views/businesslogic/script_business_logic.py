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
        DealRecordsH=RecordsHelper('deal')
        DeallineRecordsH=RecordsHelper('dealline')
        conditions=list()
        conditions.append("recordid_='00000000000000000000000000001378'")
        deal_records= DealRecordsH.get_records(conditions)
        for deal_record in deal_records:
            deal_recordid=deal_record['recordid_']
            dealline_records=DeallineRecordsH.get_records_by_linked('deal',deal_recordid)
            total_expectedcost=0
            for dealline_record in dealline_records:
                total_expectedcost=total_expectedcost+dealline_record['expectedcost']
                
        return_value=total_expectedcost
        return return_value
   

