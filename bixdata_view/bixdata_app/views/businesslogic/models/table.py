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
from .record import *

bixdata_server = os.environ.get('BIXDATA_SERVER')

class Table:
    
    def __init__(self,tableid,userid=1):
        self.db_helper=DatabaseHelper('default')
        self.tableid=tableid
        self.userid=userid
        self.context=''
        self.helper=LogicHelper()
    
    def get_records(self,viewid='',searchTerm='', conditions_list=list(),fields=None,offset=0,limit=None,orderby='recordid_ desc'):
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
                
        conditions="deleted_='N'"
        #conditions=conditions+f" AND dealname like '%{searchTerm}%' " 
        for condition in conditions_list:
            conditions=conditions+f" AND {condition}"   
            
        with connection.cursor() as cursor:
            sql=f"SELECT {select_fields} from user_{self.tableid} where {conditions} ORDER BY {orderby}"
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
    
    def get_record_by_condition(self,conditions_list=list()):
        records=self.get_records('','',conditions_list)
        if(records):
            recordid=records[0]['recordid_']
            return Record(self.tableid,recordid)
        return None
    
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
    
    
    def get_fields(self):
        print("FUN:get_fields")
        #t=Table(self.tableid)
        #fields=t.get_fields(context)
        #fields_values=self.fields
        #return list()
        post = {
            'tableid': self.tableid,
            'userid': self.userid,
            'context': self.context
        }
        print(post)
        response = requests.post(f"{bixdata_server}bixdata/index.php/rest_controller/get_record_fields", data=post)
        print(response.text)
        response_dict = json.loads(response.text)

       # if (ticketid):
        #    response_dict['Dati']['_recordidticket']['valuecode'][0]['value'] = ticketid
         #   response_dict['Dati']['_recordidticket']['valuecode'][0]['code'] = recordid_ticket

        #if tableid == 'timetracking':
         #   start = response_dict['Dati']['start']['valuecode'][0]['value']

          #  if start == '':
           #     response_dict['Dati']['start']['value'] = datetime.datetime.now().strftime("%H:%M")
        return response_dict
    

