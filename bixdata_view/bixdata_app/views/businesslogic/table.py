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
import os
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
from ..beta import *
from .database_helper import *

bixdata_server = os.environ.get('BIXDATA_SERVER')

class Table:
    
    def __init__(self,tableid,userid=1):
        self.db_helper=DatabaseHelper('default')
        self.tableid=tableid
        self.userid=userid
        self.helper=LogicHelper()
    
    def get_records(self,viewid='',searchTerm='', conditions_list=list(),fields=None,offset=0,limit=None):
        """Ottieni elenco record in base ai parametri di ricerca

        Args:
            viewid (str, optional): vista applicata. Defaults to ''.
            searchTerm (str, optional): termine generico da cercare in tutti i campi. Defaults to ''.
            conditions_list (_type_, optional): condizioni specifiche sui campi. Defaults to list().

        Returns:
            _type_: lista di dict dei risultati
        """ 
        select_fields='*'
        if fields:
            select_fields=''
            for field in fields:
                if select_fields!='':
                    select_fields=select_fields+','
                select_fields=select_fields+field
                
        conditions="True"
        conditions=conditions+f" AND dealname like '%{searchTerm}%' " 
        for condition in conditions_list:
            conditions=conditions+f" AND {condition}"   
            
        with connection.cursor() as cursor:
            sql=f"SELECT {select_fields} from user_{self.tableid} where {conditions}"
            cursor.execute(sql)
            records = self.helper.dictfetchall(cursor)
        return records
   
    def get_records_by_linked(self,linked_tableid,linked_recordid):
        LogicH=LogicHelper()
        with connection.cursor() as cursor:
            sql=f"SELECT * from user_{self.tableid} where recordid{linked_tableid}_='{linked_recordid}'"
            cursor.execute(sql)
            records = self.helper.dictfetchall(cursor)
        return records
    
    def get_records_kanban(self,viewid='',searchTerm='', conditions_list=list()):
        records=self.get_records(viewid,searchTerm,conditions_list)
        group_field='dealstage'
        groups=dict()
        for record in records:
            groupby_field_value=record[group_field]
            if groupby_field_value in groups:
                groups[groupby_field_value]['records'].append(groupby_field_value)
            else:
                groups[groupby_field_value]['description']=groupby_field_value
                groups[groupby_field_value]['records']=list()
                groups[groupby_field_value]['records'].append(groupby_field_value)
        return records
    
    def get_fields(self,context):
        fields=self.db_helper.sql_query(f"SELECT * FROM sys_user_field_order WHERE userid={self.userid} AND tableid='{self.tableid}' AND typepreference='{context}'")
        return fields
    

