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
from .record import *
from .table import *
from .database_helper import *
 


class ScriptLogic:
    
    def __init__(self):
        self.test=None
    
    def update_deals(self):
        log=''
        return_value=False
        deal_table_obj=Table('deal')
        dealline_table_obj=Table('dealline')
        adiuto_db_helper_obj=DatabaseHelper('adiuto')
        bixdata_db_helper_obj=DatabaseHelper('default')
        
        conditions=list()
        conditions.append("recordid_='00000000000000000000000000001375'")
        deal_records= deal_table_obj.get_records(conditions)
        for deal_record in deal_records:
            log+=f"Deal: {deal_record['dealname']}"
            recordid_deal=deal_record['recordid_']
            deal_record_obj=Record('deal',deal_record['recordid_'])
            adi_deal_dict = adiuto_db_helper_obj.sql_query_row(f"SELECT * FROM VA1028 WHERE F1052='{recordid_deal}' AND FENA=-1")
            deal_record_obj.set_field('dealstage',adi_deal_dict['F1033'])
            deal_record_obj.set_field('adiuto_tech',adi_deal_dict['F1067'])
            
            hubspot_dealuser=deal_record['dealuser']
            deal_type=deal_record['type']
            hubspot_id=deal_record['hubspot_id']
            bix_dealuser_dict= bixdata_db_helper_obj.sql_query_row(f"SELECT * FROM sys_user WHERE hubspot_dealuser='{hubspot_dealuser}'")
            if bix_dealuser_dict:
                deal_record_obj.set_field('dealuser1',bix_dealuser_dict['id'])
                deal_record_obj.set_field('adiuto_dealuser',bix_dealuser_dict['adiutoid'])
            
            deal_record_obj.save()
            
            #Aggiornamento dettagli deal e calcolo totali    
            dealline_records=dealline_table_obj.get_records_by_linked('deal',recordid_deal)
            total_expectedcost=0
            for dealline_record in dealline_records:
                dealline_recordid=dealline_record['recordid_']
                adiuto_dealline = adiuto_db_helper_obj.sql_query_row(f"SELECT * FROM A1029 WHERE F1062='{recordid_deal}'")
                if adiuto_dealline:
                    bix_dealline=Record('dealline',dealline_recordid)
                    bix_dealline.fields['uniteffectivecost']=adiuto_dealline['F1043']
                    bix_dealline.save()
                        
                        
                total_expectedcost=total_expectedcost+dealline_record['expectedcost']
                
        return log
   

