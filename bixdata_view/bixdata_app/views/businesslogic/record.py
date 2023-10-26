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
from .database_helper import *

class Record:
    
    def __init__(self, tableid, recordid=None):
        self.db_helper=DatabaseHelper('default')
        self.tableid=tableid
        self.recordid=recordid
        self.fields=dict()
    
    def get_recordid(self):
        return self.recordid
        
    def save(self):
        if self.recordid:
            counter=0
            sql=f"UPDATE user_{self.tableid} SET "
            for key,value in self.fields.items():
                if counter>0:
                    sql=sql+","
                sql=sql+f" {key}='{value}' "
                counter+=1
            sql=sql+f" WHERE recordid_='{self.recordid}'"   
        else:
            sql=""
        self.db_helper.sql_execute(sql)
    
    def set_field(self,field_key,field_value):    
        self.fields[field_key]=field_value   
                
    def get_field(self,field_key):
        return self.fields[field_key]    
            
        
   


