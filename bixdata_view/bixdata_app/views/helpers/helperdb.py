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


class Helperdb:
    database='default'

    @classmethod
    def sql_query(cls,sql):
        with connections[cls.database].cursor() as cursor:
            cursor.execute(sql)
            rows = cls.dictfetchall(cursor)
        return rows
    
    @classmethod
    def sql_query_row(cls,sql):
        rows=cls.sql_query(sql)
        if rows:
            return rows[0]
        else:
            return None
        
    @classmethod
    def sql_execute(cls,sql):
        with connections[cls.database].cursor() as cursor:
            cursor.execute(sql)
        return True
   
    @classmethod
    def dictfetchall(cls,cursor):
        "Return all rows from a cursor as a dict"
        columns = [col[0] for col in cursor.description]
        return [
            dict(zip(columns, row))
            for row in cursor.fetchall()
        ]


    @classmethod
    def db_get(cls,table,columns='*',conditions='true',order='',limit=''):
        if order!='':
            order=f"ORDER BY {order}"
        if limit!='':
            limit=f"LIMIT {limit}"
        sql = f"""
            SELECT {columns}
            FROM {table}
            WHERE {conditions}
            {order}
            {limit}
        """
        rows=cls.sql_query(sql)
        return rows
    
    @classmethod
    def db_get_row(cls,table,columns='*',conditions='true',order=''):
        rows= cls.db_get(table,columns,conditions,order,1)
        if rows:
            row=rows[0]
        else:
            row=None

        return row
    
    @classmethod
    def db_get_value(cls,table,column='',conditions='true',order=''):
        row= cls.db_get_row(table,column,conditions,order)
        if row:
            value=row[column]
        else:
            value=None
        return value