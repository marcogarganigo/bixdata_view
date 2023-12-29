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
from .database_helper import *


class SettingsBusinessLogic:
    
    def __init__(self):
        self.test=None
    
    def get_user_tables(self,userid):
        returnvalue=dict()
        subquery = SysUserTableOrder.objects.filter(tableid=OuterRef('id'),userid=userid).values('tableorder')[:1]
        tables=dict()
        tablesdict=dict()
        workspaces=dict()
        workspace_rows=SysTableWorkspace.objects.all()
        for workspace_row in workspace_rows:
            workspaces[workspace_row.name]=dict()
            workspaces[workspace_row.name]['name']=workspace_row.name
            workspace_name=workspace_row.name
            tablesdict=SysTable.objects.annotate(order=Subquery(subquery)).filter(workspace=workspace_name).order_by('workspace','order').values('id','description','workspace','order') 
            print(tablesdict.query) 
            workspaces[workspace_row.name]['tables']=tablesdict
        return workspaces


    def get_search_column_results(self,userid,tableid, fields_type):
        dbh=DatabaseHelper()
        subquery = SysUserFieldOrder.objects.filter(fieldid=OuterRef('id')).filter(typepreference=fields_type).values('fieldorder')[:1]
        fields=SysField.objects.annotate(order=Subquery(subquery)).filter(tableid=tableid).order_by('order').values('id','fieldid','tableid','order','description')
        
        sql1=f"SELECT sys_field.id,sys_field.fieldid,sys_field.tableid,sys_user_field_order.fieldorder,description,sys_field.label FROM sys_field LEFT JOIN sys_user_field_order ON sys_field.id=sys_user_field_order.fieldid WHERE sys_field.tableid='{tableid}' AND  sys_user_field_order.userid={userid} AND sys_user_field_order.typepreference='{fields_type}' ORDER BY sys_field.label, sys_user_field_order.fieldorder"
        fields1=dbh.sql_query(sql1)
        
        sql2=f"""
        SELECT sys_field.id,sys_field.fieldid,sys_field.tableid,NULL AS fieldorder,sys_field.description,sys_field.label
        FROM sys_field
        WHERE tableid='{tableid}' AND sys_field.id
        NOT IN
        (
        SELECT sys_user_field_order.fieldid
        FROM sys_user_field_order
        WHERE
        tableid='{tableid}' AND userid={userid} AND typepreference='{fields_type}'
        )
        ORDER BY sys_field.label, sys_field.fieldid
        """
        fields2=dbh.sql_query(sql2)
        
        fields=fields1+fields2
        return fields
    
    def get_usersettings(self,bixid):
        userid=SysUser.objects.get(bixid=bixid).id
        us=UserSettings(userid)
        return us
    
    
class UserSettings:
    userid=0
    record_open_layout='rightcard'
    theme='default'
    active_panel='table'
    def __init__(self,user_id):
        userid=user_id
        
    def get_fieldsorder(tableid,typepreference):
        subquery = SysUserFieldOrder.objects.filter(fieldid=OuterRef('id')).filter(typepreference=typepreference).values('fieldorder')[:1]
        fields=SysField.objects.annotate(order=Subquery(subquery)).filter(tableid=tableid).order_by('order').values('id','fieldid','tableid','order')
        return fields

        
