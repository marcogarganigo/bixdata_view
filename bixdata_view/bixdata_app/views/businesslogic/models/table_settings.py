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
# from bixdata_app.models import MyModel
from django import template
from bs4 import BeautifulSoup
from django.db.models import OuterRef, Subquery
from ..logic_helper import *
from .database_helper import *

bixdata_server = os.environ.get('BIXDATA_SERVER')


class TableSettings:
    settings = {
        'edit': {
            'type': 'select',
            'options': ['true', 'false'],
            'value': 'true'
        },
        'risultati_edit': {
            'type': 'select',
            'options': ['true', 'false'],
            'value': 'false'
        },
        'autosave': {
            'type': 'select',
            'options': ['true', 'false'],
            'value': 'true'
        },
        'delete': {
            'type': 'select',
            'options': ['true', 'false'],
            'value': 'true'
        },
        'hidden': {
            'type': 'select',
            'options': ['true', 'false'],
            'value': 'false'
        },
        'menu': {
            'type': 'select',
            'options': ['true', 'false'],
            'value': 'false'
        },
        'icon_type': {
            'type': 'select',
            'options': ['fontawesome', 'material'],
            'value': 'fontawesome'
        },
        'icon': {
            'type': 'parola',
            'value': 'database'
        },
        'customview_list': {
            'type': 'select',
            'options': ['true', 'false'],
            'value': 'false'
        },
        'customview_card': {
            'type': 'select',
            'options': ['true', 'false'],
            'value': 'false'
        },
        'scheda_layout': {
            'type': 'select',
            'options': ['standard_dati', 'standard_allegati', 'allargata'],
            'value': 'standard_dati'
        },
        'scheda_mostratutti': {
            'type': 'select',
            'options': ['true', 'false'],
            'value': 'false'
        },
        'popup_layout': {
            'type': 'select',
            'options': ['standard_dati', 'standard_allegati', 'allargata'],
            'value': 'standard_dati'
        },
        'popup_width': {
            'type': 'select',
            'options': ['30', '60', '90'],
            'value': '60'
        },
        'scheda_record_width': {
            'type': 'select',
            'options': ['25', '42', '48', '57', '98'],
            'value': '25'
        },
        'allargata_dati_width': {
            'type': 'parola',
            'value': '50'
        },
        'scheda_ricerca_display': {
            'type': 'select',
            'options': ['true', 'false'],
            'value': 'true'
        },
        'scheda_ricerca_width': {
            'type': 'select',
            'options': ['20', '42', ''],
            'value': '20'
        },
        'scheda_ricerca_default': {
            'type': 'select',
            'options': ['filtri', 'ricerche_salvate'],
            'value': 'filtri'
        },
        'ricerca_lockedview': {
            'type': 'select',
            'options': ['true', 'false'],
            'value': 'false'
        },
        'risultati_limit': {
            'type': 'parola',
            'value': '50'
        },
        'risultati_layout': {
            'type': 'select',
            'options': ['righe', 'table', 'preview', 'badge', 'report', 'calendar'],
            'value': 'righe'
        },
        'risultati_width': {
            'type': 'select',
            'options': ['42', '48', '57', '98'],
            'value': '57'
        },
        'risultati_border': {
            'type': 'select',
            'options': ['1px solid transparent', '1px solid #dedede'],
            'value': '1px solid transparent'
        },
        'risultati_font_size': {
            'type': 'select',
            'options': ['6', '8', '10', '12', '14', '16', '18'],
            'value': '14'
        },
        'risultati_open': {
            'type': 'select',
            'options': ['right', 'down', 'popup'],
            'value': 'right'
        },
        'risultati_new': {
            'type': 'select',
            'options': ['right', 'down', 'popup'],
            'value': 'right'
        },
        'risultati_order': {
            'type': 'select',
            'options': ['asc', 'desc', ''],
            'value': 'desc'
        },
        'risultati_showreport': {
            'type': 'select',
            'options': ['true', 'false', ''],
            'value': 'false'
        },
        'risultati_showcalendar': {
            'type': 'select',
            'options': ['true', 'false', ''],
            'value': 'false'
        },
        'risultati_anteprima_aspectratio': {
            'type': 'select',
            'options': ['2:3', '3:2', '16:9'],
            'value': '2:3'
        },
        'risultati_stampa_elenco_orientamento': {
            'type': 'select',
            'options': ['portrait', 'landscape', ''],
            'value': 'portrait'
        },
        'linked_layout': {
            'type': 'select',
            'options': ['righe', 'preview', 'badge'],
            'value': 'righe'
        },
        'linked_open': {
            'type': 'select',
            'options': ['right', 'down', 'popup'],
            'value': 'down'
        },
        'linked_new': {
            'type': 'select',
            'options': ['right', 'down', 'popup'],
            'value': 'popup'
        },
        'linked_rows': {
            'type': 'select',
            'options': ['5', '10', '15', '20', '25', '30'],
            'value': '5'
        },
        'linked_label_opened': {
            'type': 'select',
            'options': ['true', 'false'],
            'value': 'false'
        },
        'pages_display': {
            'type': 'select',
            'options': ['true', 'false'],
            'value': 'true'
        },
        'pages_fileupload_display': {
            'type': 'select',
            'options': ['true', 'false'],
            'value': 'true'
        },
        'pages_view': {
            'type': 'select',
            'options': ['thumbnail', 'name', 'detail'],
            'value': 'thumbnail'
        },
        'pages_scheda_layout': {
            'type': 'select',
            'options': ['list', 'grid', 'hidden'],
            'value': 'list'
        },
        'pages_popup_layout': {
            'type': 'select',
            'options': ['list', 'grid', 'hidden'],
            'value': 'list'
        },
        'pages_thumbnail_show': {
            'type': 'select',
            'options': ['true', 'false', ''],
            'value': 'true'
        },
        'default_save': {
            'type': 'select',
            'options': ['salva', 'salva e chiudi', 'salva e nuovo', 'salva e nuovo-salva e chiudi',
                        'allega salva e nuovo', 'salva e ripeti'],
            'value': 'salva'
        },
        'default_viewid': {
            'type': 'parola',
            'value': '0'
        },
        'default_recordstab': {
            'type': 'parola',
            'value': 'Tabella'
        },
        'default_recordtab': {
            'type': 'parola',
            'value': 'Fields'
        },
        'dem_mail_field': {
            'type': 'select',
            'options': ['address', 'bexio_contact_type_id', 'bexio_status', 'cap', 'city', 'companyname',
                        'customertype', 'email', 'ictpbx_price', 'id', 'id_bexio', 'id_vte', 'note', 'paymentstatus',
                        'phonenumber', 'recordidcontact_', 'recordiddealline_', 'recordiddeal_', 'recordidinvoiceline_',
                        'recordidinvoice_', 'recordidprojectmilestone_', 'recordidproject_', 'recordidsalesorderline_',
                        'recordidsalesorderplannedinvoice', 'recordidsalesorder_', 'recordidserviceandasset_',
                        'recordidservicecontract_', 'recordidtask_', 'recordidticket_', 'recordidtimesheet_',
                        'recordiduser_log_', 'recordid_jdoc', 'salesperson_text', 'salesuser', 'scn', 'sector',
                        'servizitxt', 'state', 'status', 'sw_price', 'tipo', 'travelkm_price', 'travel_price',
                        'vatnumber', 'website'],
            'value': 'address'
        },
        'fields_autoscroll': {
            'type': 'select',
            'options': ['true', 'false'],
            'value': 'false'
        },
        'col_s': {
            'type': 'parola',
            'value': '3'
        },
        'col_m': {
            'type': 'parola',
            'value': '3'
        },
        'col_l': {
            'type': 'parola',
            'value': '3'
        },
    }

    def __init__(self, tableid, userid=1):
        self.db_helper = DatabaseHelper('default')
        self.tableid = tableid
        self.userid = userid
        self.settings = self.get_settings()

    def get_settings(self):
        settings_copy = {key: value.copy() for key, value in self.settings.items()}

        sql = f"SELECT settingid, value FROM sys_user_table_settings WHERE tableid='{self.tableid}' AND userid='{self.userid}'"
        rows = self.db_helper.sql_query(sql)

        for setting_id, setting_info in settings_copy.items():
            for row in rows:
                if setting_id == row['settingid']:
                    setting_info['value'] = row['value']

        return settings_copy

    def save(self):
        table_settings = self.settings

        # if self.tableid:

        success = True

        for setting in table_settings:

            sql_delete = f"DELETE FROM sys_user_table_settings WHERE tableid='{self.tableid}' AND settingid='{setting}' AND userid='{self.userid}' "
            self.db_helper.sql_execute(sql_delete)

            sql_insert = f"INSERT INTO sys_user_table_settings (userid, tableid, settingid, value) VALUES " \
                         f"('{self.userid}', '{self.tableid}', '{setting}', '{table_settings[setting]['value']}')"
            try:
                self.db_helper.sql_execute(sql_insert)
                print(f"Inserted setting {setting}")
            except Exception as e:
                print(f"Error inserting setting {setting}: {e}")
                success = False

        return success
