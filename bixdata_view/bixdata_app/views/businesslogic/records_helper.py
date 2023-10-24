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
from .logic_helper import *


class RecordsHelper:
    
    def __init__(self,tableid):
        self.tableid=tableid
    
    
    def get_records(self, conditions_list=list()):
        LogicHelper=LogicHelper()
        conditions="True"
        for condition in conditions_list:
            conditions=conditions+f" AND {condition}"   
            
        with connection.cursor() as cursor:
            sql=f"SELECT * from user_{self.tableid} where {conditions}"
            cursor.execute(sql)
            records = LogicHelper.dictfetchall(cursor)
        return records
   
    def get_records_by_linked(self,linked_tableid,linked_recordid):
        LogicHelper=LogicHelper()
        with connection.cursor() as cursor:
            sql=f"SELECT * from user_{self.tableid} where recordid{linked_recordid}_='{linked_recordid}'"
            cursor.execute(sql)
            records = LogicHelper.dictfetchall(cursor)
        return records
