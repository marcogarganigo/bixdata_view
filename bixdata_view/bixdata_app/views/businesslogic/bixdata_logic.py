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


class BixdataLogic:
    

    @classmethod    
    def get_menu_tables(cls,userid):
        userid=1
        subquery = SysUserTableOrder.objects.filter(tableid=OuterRef('id'),userid=userid).values('tableorder')[:1]
        tables=dict()
        workspaces=dict()
        workspace_rows=SysTableWorkspace.objects.all()
        for workspace_row in workspace_rows:
            workspaces[workspace_row.name]=dict()
            workspaces[workspace_row.name]['workspaceid']=workspace_row.workspaceid
            workspaces[workspace_row.name]['name']=workspace_row.name
            workspaces[workspace_row.name]['icon']=workspace_row.icon
            workspace_name=workspace_row.name
            tables=list(SysTable.objects.annotate(order=Subquery(subquery)).filter(workspace=workspace_name).filter(order__isnull=False).order_by('workspace','order').values('id','description','workspace','order'))
            workspaces[workspace_row.name]['tables']=tables
        workspace2=dict()    
        for key,workspace in workspaces.items():
            if len(workspace['tables'])>0:
                workspace2[key]=workspace
        return workspace2




    