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
        deal_table_obj=Table('deal')
        dealline_table_obj=Table('dealline')
        adiuto_db_obj=DatabaseHelper('adiuto')
        bixdata_db_obj=DatabaseHelper('default')
        
        conditions=list()
        conditions.append("syncstatus='Si'")
        #conditions.append("recordid_='00000000000000000000000000001421'")
        deal_records= deal_table_obj.get_records(conditions)
        for deal_record_dict in deal_records:
            log+=f"Deal: {deal_record_dict['dealname']} <br/><br/>"
            print(f"Deal: {deal_record_dict['dealname']} <br/><br/>")
            recordid_deal=deal_record_dict['recordid_']
            deal_record_obj=Record('deal',recordid_deal)
            project_dict= bixdata_db_obj.sql_query_row(f"SELECT * FROM user_project WHERE recordiddeal_='{recordid_deal}'")
            if project_dict:
                self.update_project(project_dict['recordid_'])
            
            project_record_obj=Record('project',project_dict['recordid_'])
            hubspot_dealuser=deal_record_obj.get_field('dealuser')
                       
            
            dealuser_dict= bixdata_db_obj.sql_query_row(f"SELECT * FROM sys_user WHERE hubspot_dealuser='{hubspot_dealuser}'")
            if dealuser_dict:
                deal_record_obj.set_field('dealuser1',dealuser_dict['id'])
                deal_record_obj.set_field('adiuto_dealuser',dealuser_dict['adiutoid'])
            
            adi_deal_dict = adiuto_db_obj.sql_query_row(f"SELECT * FROM VA1028 WHERE F1052='{recordid_deal}' AND FENA=-1")
            deal_record_obj.set_field('dealstage',adi_deal_dict['F1033'])
            deal_record_obj.set_field('adiuto_tech',adi_deal_dict['F1067'])
            dealtech_dict= bixdata_db_obj.sql_query_row(f"SELECT * FROM sys_user WHERE hubspot_dealuser='{hubspot_dealuser}'")
            if dealtech_dict:
                deal_record_obj.set_field('project_assignedto',dealtech_dict['id'])
            
            
            
            #Aggiornamento dettagli deal e calcolo totali    
            dealline_records=dealline_table_obj.get_records_by_linked('deal',recordid_deal)
            total_actualcost=0
            total_expectedcost=0
            total_price=0
            total_expectedhours=0
            for dealline_record_dict in dealline_records:
                #quantity
                #unitprice
                #price
                #unitexpectedcost
                #expectedcost
                #expectedmargin
                #uniteffectivecost
                #effectivecost
                #quantity_actual
                #quantity_difference
                #price_actual
                #price_difference
                #margin_actual
                dealline_record_obj=Record('dealline',dealline_record_dict['recordid_'])
                adiuto_dealline_dict = adiuto_db_obj.sql_query_row(f"SELECT * FROM VA1029 WHERE FENA=-1 AND F1062='{dealline_record_obj.get_field('recordid_')}'")
                if adiuto_dealline_dict:
                    adiuto_uniteffectivecost=0
                    if adiuto_dealline_dict['F1043']:
                        adiuto_uniteffectivecost=float(adiuto_dealline_dict['F1043'])
                    dealline_record_obj.set_field('uniteffectivecost',adiuto_uniteffectivecost)
                dealline_record_obj.set_field('effectivecost',(dealline_record_obj.get_field('quantity') or 0)*(dealline_record_obj.get_field('uniteffectivecost') or 0))
                dealline_record_obj.save()        
                
                if dealline_record_obj.get_field('effectivecost')>0:        
                    total_actualcost=total_actualcost+dealline_record_obj.get_field('effectivecost')
                else:
                    if dealline_record_obj.get_field('expectedhours')==None or dealline_record_obj.get_field('expectedhours')==0:
                        total_actualcost=total_actualcost+(dealline_record_obj.get_field('expectedcost') or 0)
                        total_expectedhours=total_expectedhours+(deal_record_obj.get_field('expectedhours') or 0)
                total_expectedcost=total_expectedcost+(dealline_record_obj.get_field('expectedcost') or 0)
                total_price=total_price+(dealline_record_obj.get_field('price') or 0)
                
            deal_record_obj.set_field('usedhours',project_record_obj.get_field('usedhours'))
            total_actualcost=total_actualcost+((project_record_obj.get_field('usedhours') or 0)*60)
            if deal_record_obj.get_field('amount')==None:
                deal_record_obj.set_field('amount',0)
            deal_record_obj.set_field('actualcost',total_actualcost)
            deal_record_obj.set_field('expectedcost',total_expectedcost)
            deal_record_obj.set_field('totalprice',total_price)
            deal_record_obj.set_field('expectedmargin', (deal_record_obj.get_field('totalprice') or 0) - total_expectedcost)
            if total_actualcost>0:
                deal_record_obj.set_field('effectivemargin', (deal_record_obj.get_field('totalprice') or 0) - total_actualcost)
                deal_record_obj.set_field('margindifference',(deal_record_obj.get_field('effectivemargin') or 0) - (deal_record_obj.get_field('expectedmargin') or 0) )
                if (deal_record_obj.get_field('expectedmargin') or 0)!=0:
                    deal_record_obj.set_field('margindifference_perc',(deal_record_obj.get_field('margindifference') or 0) / (deal_record_obj.get_field('expectedmargin') or 0) * 100 )
            else:
                deal_record_obj.set_field('effectivemargin',0)
                deal_record_obj.set_field('margindifference',0)
                deal_record_obj.set_field('margindifference_perc',0)
            deal_record_obj.set_field('expectedhours',total_expectedhours)
            
            
            deal_record_obj.save()
                
        return log
   

    def update_project(self,project_recordid):
        """Aggiorna le ore effettive in base ai timesheet registrati

        Args:
            project_recordid (str): identificativo del progetto da aggiornare
        """
        project_record_obj=Record('project',project_recordid)
        timesheet_table_obj=Table('timesheet')
        timesheets=timesheet_table_obj.get_records_by_linked('project',project_recordid)
        usedhours=0
        for timesheet_dict in timesheets:
            usedhours=usedhours+(timesheet_dict['totaltime_decimal'] or 0)
        project_record_obj.set_field('usedhours',usedhours)
        project_record_obj.save()