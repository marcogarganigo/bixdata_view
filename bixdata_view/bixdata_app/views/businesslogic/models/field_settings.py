from django.contrib.sessions.models import Session
from bixdata_app.models import *
import os
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
from ..logic_helper import *
from .database_helper import *

bixdata_server = os.environ.get('BIXDATA_SERVER')

class FieldSettings:
    
    settings = {
        'obbligatorio': {
            'options': ['true', 'false'],
            'value': 'false'
        },
        'calcolato': {
            'options': ['true', 'false'],
            'value': 'false'
        },
        'calcolato': {
            'options': [],
            'value': 'false'
        }
    }
    
    def __init__(self, tableid, fieldid, userid=1):
        self.db_helper=DatabaseHelper('default')
        self.tableid=tableid
        self.fieldid=fieldid
        self.userid=userid
        self.settings=FieldSettings.settings
        
        
        
    def get_settings(self):
        return self.settings
    
    def save(self):

        field_settings=self.settings

        if self.tableid and self.fieldid:
            sql = f"DELETE FROM sys_user_field_settings WHERE tableid='{self.tableid}' AND fieldid='{self.fieldid}' AND userid='{self.userid}' "
            self.db_helper.sql_execute(sql)

        for setting in field_settings:

            sql=f"INSERT INTO sys_user_field_settings (userid, tableid, fieldid, settingid, value) VALUES " \
                f"('{self.userid}', '{self.tableid}', '{self.fieldid}', '{setting}', '{field_settings[setting]['value']}')"
            self.db_helper.sql_execute(sql)
            return True
        return False
        
   
    
        
        
    
 
   


