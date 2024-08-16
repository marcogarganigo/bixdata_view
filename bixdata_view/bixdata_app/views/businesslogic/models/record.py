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
from ...helpers.helperdb import *

bixdata_server = os.environ.get('BIXDATA_SERVER')

class Record:
    
    def __init__(self, tableid, recordid=None, userid=1):
        self.db_helper=DatabaseHelper('default')
        self.tableid=tableid
        self.recordid=recordid
        self.userid=userid
        self.master_tableid=''
        self.master_recordid=''
        self.context='insert_fields'
        if recordid:
            self.fields=self.db_helper.sql_query_row(f"SELECT * FROM user_{self.tableid} WHERE recordid_='{self.recordid}'")
        else:
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
                if value!=None:  
                    if type(value)==str:
                        value = value.replace("'", "''")  
                    sql=sql+f" {key}='{value}' "
                else:
                    sql=sql+f" {key}=null "
                counter+=1
            sql=sql+f" WHERE recordid_='{self.recordid}'"  
            self.db_helper.sql_execute(sql) 
        else:
            sqlmax=f"SELECT MAX(recordid_) as max_recordid FROM user_{self.tableid}"
            result=Helperdb.sql_query_row(sqlmax)
            max_recordid=result['max_recordid']
            if max_recordid is None:
                next_recordid = '00000000000000000000000000000001'
            else:
                next_recordid = str(int(max_recordid) + 1).zfill(32)
            
            sqlmax=f"SELECT MAX(id) as max_id FROM user_{self.tableid}"
            result=Helperdb.sql_query_row(sqlmax)
            max_id=result['max_id']
            if max_id is None:
                next_id = 1
            else:
                next_id = max_id+1
            
            current_datetime=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            sqlinsert=f"INSERT INTO user_{self.tableid} (recordid_,creatorid_,creation_,id) VALUES ('{next_recordid}',{self.userid},'{current_datetime}',{next_id}) "
            self.db_helper.sql_execute(sqlinsert)
            self.recordid=next_recordid
            self.save()
        
    
    def set_field(self,field_key,field_value): 
        self.fields[field_key]=field_value   
                
    def get_field(self,field_key):
        return self.fields[field_key]    
            
    def get_linkedtables():
        return dict()
    
    def get_linkedrecords(self,linkedtable):
        if linkedtable=='salesorderline':
            records=self.db_helper.sql_query(f"SELECT * FROM user_{linkedtable} WHERE recordid{self.tableid}_='{self.recordid}' AND deleted_='N' AND status='In Progress' ")
        else:
            records=self.db_helper.sql_query(f"SELECT * FROM user_{linkedtable} WHERE recordid{self.tableid}_='{self.recordid}' AND deleted_='N' ")
        return records   
    
    def get_fields(self):
        #t=Table(self.tableid)
        #fields=t.get_fields(context)
        #fields_values=self.fields
        #return list()
        post = {
            'tableid': self.tableid,
            'recordid': self.recordid,
            'userid': self.userid,
            'master_tableid': self.master_tableid,
            'master_recordid': self.master_recordid,
            'context': self.context
        }

        response = requests.post(f"{bixdata_server}bixdata/index.php/rest_controller/get_record_fields", data=post)

        response_dict = json.loads(response.text)

        #TODO generalizzare con le impostazioni per data di default ad oggi
        if self.tableid=='salespush':
            if  response_dict['Dati']['recalldate']['valuecode'][0]['code'] == '':
                response_dict['Dati']['recalldate']['valuecode'][0]['value']=datetime.datetime.now().strftime("%Y-%m-%d")
                response_dict['Dati']['recalldate']['valuecode'][0]['code']=datetime.datetime.now().strftime("%Y-%m-%d")

        if self.tableid=='salespush':
            if  response_dict['Dati']['lastcalldate']['valuecode'][0]['code'] == '':
                response_dict['Dati']['lastcalldate']['valuecode'][0]['value']=datetime.datetime.now().strftime("%Y-%m-%d")
                response_dict['Dati']['lastcalldate']['valuecode'][0]['code']=datetime.datetime.now().strftime("%Y-%m-%d")
 
       # if (ticketid):
        #    response_dict['Dati']['_recordidticket']['valuecode'][0]['value'] = ticketid
         #   response_dict['Dati']['_recordidticket']['valuecode'][0]['code'] = recordid_ticket

        #if tableid == 'timetracking':
         #   start = response_dict['Dati']['start']['valuecode'][0]['value']

          #  if start == '':
           #     response_dict['Dati']['start']['value'] = datetime.datetime.now().strftime("%H:%M")
        return response_dict
    
        
        
    
 
   


