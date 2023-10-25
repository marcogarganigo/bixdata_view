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


class DatabaseHelper:
    database=''
    
    def __init__(self, database='default'):
        self.database=database
    
    def get_recordid(self):
        return self.recordid
        
    def insert(self):
        return True
    
    def update(self):
        return True
    
    def sql_query(self,sql):
        with connections[self.database].cursor() as cursor:
            cursor.execute(sql)
            rows = self.dictfetchall(cursor)
        return rows
    
    def sql_query_row(self,sql):
        rows=self.sql_query(sql)
        if rows:
            return rows[0]
        else:
            return None
        
    
    def sql_execute(self,sql):
        with connections[self.database].cursor() as cursor:
            cursor.execute(sql)
        return True
   
    def dictfetchall(self,cursor):
        "Return all rows from a cursor as a dict"
        columns = [col[0] for col in cursor.description]
        return [
            dict(zip(columns, row))
            for row in cursor.fetchall()
        ]
