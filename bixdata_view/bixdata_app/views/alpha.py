import tempfile
import uuid
import threading
from django.contrib.sessions.models import Session
import threading
from bixdata_app.models import *

import pyperclip
from aiohttp.web_fileresponse import FileResponse
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect
from django.http import JsonResponse, request
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.template.loader import render_to_string
import requests
import json
import datetime
from django.contrib.auth.decorators import login_required
import time

import pdfkit

from .bixdata_view import *
from .businesslogic.office_calendar import OfficeCalendar
from ..forms import LoginForm
from django.contrib.auth.decorators import user_passes_test
from django.contrib import messages
from django.db import connection
from django.http import JsonResponse
from django.contrib.auth.models import Group, Permission, User, Group
from django_user_agents.utils import get_user_agent
import os
from django.conf import settings
from django.views.decorators.clickjacking import xframe_options_exempt
import subprocess
from .beta import *
from .helper_view import *
from htmldocx import HtmlToDocx
import csv
from functools import wraps

bixdata_server = os.environ.get('BIXDATA_SERVER')


# Questa funzione ritorna la pagina test_autocomplete.html
def get_test_autocomplete(request):
    return render(request, 'test_autocomplete.html')


# Questa funzione ritorna i dati richiesti con i select autocomplete
def get_autocomplete_data(request):
    term = request.GET.get('term')
    tableid = request.GET.get('tableid')
    mastertableid = request.GET.get('mastertableid')
    post = {
        'tableid': tableid,
        'mastertableid': mastertableid,
        'term': term
    }
    response = requests.post(f"{bixdata_server}bixdata/index.php/rest_controller/get_autocomplete_data", data=post)

    response = json.loads(response.text)

    data = ['Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange', '']
    data = [{"id": str(i), "value": item} for i, item in enumerate(
        data) if term.lower() in item.lower()]
    return JsonResponse({'data': response})


def get_full_data(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        with connection.cursor() as cursor1:
            cursor1.execute(
                "SELECT query_conditions FROM sys_view WHERE id = 10"
            )
            query = cursor1.fetchone()[0]
            # query = query.replace('namee', name)
            with connection.cursor() as cursor2:
                cursor2.execute(
                    # "select dealname, expectedmargin, effectivemargin from user_deal where dealuser = %s", [name]
                    query
                )
                rows = cursor2.fetchall()
                dealname = [row[0] for row in rows]
                expectedmargin = [row[1] for row in rows]
                effectivemargin = [row[2] for row in rows]

                dealname = str(dealname)
                dealname = dealname.split(',')

                expectedmargin = str(expectedmargin)
                expectedmargin = expectedmargin.split(',')

                effectivemargin = str(effectivemargin)
                effectivemargin = effectivemargin.split(',')

                data2 = {
                    'dealname': dealname,
                    'expectedmargin': expectedmargin,
                    'effectivemargin': effectivemargin,
                    'name': name
                }

    return JsonResponse(data2)


def get_test_query2(request):
    with connection.cursor() as cursor1:
        cursor1.execute(
            "SELECT query_conditions FROM sys_view WHERE id = 11"
        )
        query = cursor1.fetchone()[0]
        with connection.cursor() as cursor2:
            cursor2.execute(
                query
            )
            rows = cursor2.fetchall()
            amounts = [row[0] for row in rows]
            months = [row[1] for row in rows]

            for i in range(len(amounts)):
                if amounts[i] is None:
                    amounts[i] = 0

            with connection.cursor() as cursor3:
                cursor3.execute(
                    "SELECT query_conditions FROM sys_view WHERE id = 15"
                )
                query2 = cursor3.fetchone()[0]
                with connection.cursor() as cursor4:
                    cursor4.execute(
                        query2
                    )
                    rows2 = cursor4.fetchall()
                    totalnets = [row[0] for row in rows2]

            data = {
                'amounts': amounts,
                'months': months,
                'totalnets': totalnets
            }

    return render(request, 'other/test_query2.html', {'data': data})


def get_full_data2(request):
    if request.method == 'POST':
        date = request.POST.get('date')
        with connection.cursor() as cursor1:
            cursor1.execute(
                "SELECT query_conditions FROM sys_view WHERE id = 12"
            )
            query = cursor1.fetchone()[0]
            with connection.cursor() as cursor2:
                cursor2.execute(
                    # "SELECT dealname, effectivemargin FROM user_deal WHERE closedate LIKE %s", [f"{date}-%"]
                    query
                )

                rows = cursor2.fetchall()
                dealname = [row[0] for row in rows]
                effectivemargin = [row[1] for row in rows]

                dealname = str(dealname)
                dealname = dealname.split(',')

                effectivemargin = str(effectivemargin)
                effectivemargin = effectivemargin.split(',')

                data2 = {
                    'dealname': dealname,
                    'effectivemargin': effectivemargin,
                    'date': date
                }

    return JsonResponse(data2)


def get_chart3(request):
    if request.method == 'POST':
        with connection.cursor() as cursor1:
            cursor1.execute(
                "SELECT query_conditions FROM sys_view WHERE id = 13"
            )
            query = cursor1.fetchone()[0]
            with connection.cursor() as cursor2:
                cursor2.execute(
                    query
                )
                rows = cursor2.fetchall()

                deal_users = [row[0] for row in rows]
                amounts = [row[1] for row in rows]

                data = {
                    'deal_users': deal_users,
                    'amounts': amounts,
                }
                with connection.cursor() as cursor3:
                    cursor3.execute(
                        "SELECT query_conditions FROM sys_view WHERE id = 14"
                    )
                    query2 = cursor3.fetchone()[0]
                    with connection.cursor() as cursor4:
                        cursor4.execute(
                            query2
                        )
                        rows2 = cursor4.fetchall()

                        amounts2 = [row[1] for row in rows2]
                        deal_users2 = [row[0] for row in rows2]

                        data2 = {
                            'amounts2': amounts2,
                            'deal_users2': deal_users2
                        }

        return render(request, 'other/chart3.html', {'data': data, 'data2': data2})


def get_chart4(request):
    if request.method == 'POST':
        with connection.cursor() as cursor1:
            cursor1.execute(
                "SELECT query_conditions FROM sys_view WHERE id = 16"
            )
            query = cursor1.fetchone()[0]
            with connection.cursor() as cursor2:
                cursor2.execute(
                    query
                )
                rows = cursor2.fetchall()

                months = [row[0] for row in rows]
                totalnets = [row[1] for row in rows]

                data = {
                    'months': months,
                    'totalnets': totalnets,
                }

        return render(request, 'other/chart4.html', {'data': data})


# Questa funzione ritorna il loading
def get_render_loading(request):
    return render(request, 'other/loading.html')


# request: {tableid}


# Questa funzione serve per la ricerca dei record
def get_search_fields_data(tableid):
    search_fields = []
    with connection.cursor() as cursor:
        cursor.execute(
            f"SELECT f.* FROM sys_user_table_search_field AS s join sys_field as f on s.tableid=f.tableid and s.fieldid=f.fieldid  WHERE s.tableid='{tableid}'"
        )
        result = dictfetchall(cursor)
        if result:
            for field in result:
                field['fieldtype'] = field['fieldtypeid']  # Add fieldtype key to the field dictionary
                search_fields.append(field)
    return search_fields





# Questa funzione è un test per i grafici
@login_required(login_url='/login/')
def get_render_content_chart(request):
    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT dealuser, SUM(effectivemargin), sum(expectedmargin) FROM user_deal WHERE dealuser is not null GROUP BY dealuser")
        rows = cursor.fetchall()
        users = [row[0] for row in rows]
        effective_margins = [row[1] for row in rows]
        expected_margins = [row[2] for row in rows]

        data = {
            'users': users,
            'effective_margins': effective_margins,
            'expected_margins': expected_margins,
        }

    return render(request, 'records/records_chart.html', {'data': data})


@login_required(login_url='/login/')
def get_block_records_chart(request):
    context = dict()
    tableid = request.POST.get('tableid')
    post = {
        'table': 'deal',
        'searchTerm': '',
    }
    response = requests.post(
        f"{bixdata_server}bixdata/index.php/rest_controller/get_records_chart", data=post)
    response_dict = json.loads(response.text)
    label = response_dict['label']

    label = '# of test'
    labels = ['Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange']
    labels = json.dumps(labels)
    data = [12, 19, 3, 5, 2, 3]
    data = json.dumps(data)

    chart_data = list(zip(labels, data))

    records_table = render_to_string(
        'block/records/records_chart.html', chart_data, request=request)
    return HttpResponse(records_table)


# Questa funzione
@login_required(login_url='/login/')
def get_block_reload(request):
    return render(request)


# Questa funzione builda i dashboard blocks e li mette insieme nella pagina dashboard che ritorna
@login_required(login_url='/login/')
def get_render_content_dashboard(request):
    context = {}
    context['blocks'] = []  # Initialize the blocks list
    context['block_list'] = []  # Initialize the block_list list
    user_id = request.user.id

    with connection.cursor() as cursor2:

        cursor2.execute(
            "SELECT sys_user_id FROM v_users WHERE id = %s", [user_id]
        )
        bixid = cursor2.fetchone()[0]

        cursor2.execute(
            "SELECT dashboardid FROM sys_user_dashboard WHERE userid = %s", [bixid]
        )

        righe = cursor2.fetchall()
        dashboard_id = righe[0][0]
        context['dashboardid'] = dashboard_id

    if request.method == 'POST':
        selected = ''
        with connection.cursor() as cursor:

            context['userid'] = bixid

            datas = SysUserDashboardBlock.objects.filter(userid=bixid).values()

            all_blocks = SysDashboardBlock.objects.all()

            for block in all_blocks:
                context['block_list'].append(block)

            for data in datas:
                cursor.execute(
                    "SELECT * FROM v_sys_dashboard_block WHERE id = %s", [data['dashboard_block_id']]
                )
                results = dictfetchall(cursor)
                results = results[0]
                block = dict()
                block['id'] = data['id']

                block['gsx'] = data['gsx']
                block['gsy'] = data['gsy']
                block['gsw'] = data['gsw']
                block['gsh'] = data['gsh']

                # if they are null set default values
                if block['gsw'] == None or block['gsw'] == '':
                    block['gsw'] = 3
                    block['gsh'] = 2

                width = results['width']
                if width == None or width == 0 or width == '':
                    width = 4

                height = results['height']
                if height == None or height == 0 or height == '':
                    height = '50%'

                block['width'] = width
                block['height'] = height
                if results['reportid'] is None or results['reportid'] == 0:

                    tableid = results['tableid']
                    tableid = 'user_' + tableid

                    block['html'] = get_records_table(request, results['tableid'], None, None, '', results['viewid'], 1,'', '')


                else:

                    selected = ''
                    if results['operation'] == 'somma':
                        fields = results['fieldid'].split(';')
                        for field in fields:
                            field = 'SUM(' + field + ')'
                            selected += field + ','
                        groupby = results['groupby']
                        selected += groupby

                    query_conditions = results['query_conditions']
                    userid = get_userid(request.user.id)
                    query_conditions = query_conditions.replace("$userid$", str(userid))
                    id = data['id']
                    tableid = results['tableid']
                    name = results['name']
                    layout = results['layout']
                    sql = "SELECT " + selected + " FROM " + 'user_' + tableid + \
                          " WHERE " + query_conditions + " GROUP BY " + groupby
                    block['sql'] = sql
                    block['html'] = get_chart(request, sql, id, name, layout, fields)
                    context['userid'] = userid
                context['blocks'].append(block)

    return user_agent(request, 'content/dashboard.html', 'content/dashboard_mobile.html', context)


# Questa funzione serve per salvare le posizioni e le dimensioni dei blocchi della dashboard
def save_block_order(request):
    values = request.POST.get('value_list')

    values = json.loads(values)
    print(values)
    for value in values:
        record_id = value.get('id')
        gsx = value.get('gsX')
        gsy = value.get('gsY')
        gsw = value.get('gsW')
        gsh = value.get('gsH')

        if record_id is not None:
            SysUserDashboardBlock.objects.filter(id=record_id).update(gsx=gsx, gsy=gsy, gsw=gsw, gsh=gsh)

    return JsonResponse({'success': True})


# Questa funzione prende in input i dati per comporre i grafici e ritorna il template del tipo di grafico in base alla variabile layout_chart
@login_required(login_url='/login/')
def get_chart(request, sql, id, name, layout, fields):
    query = sql
    id_sql = id
    name_chart = name
    layout_chart = layout
    fields_chart = fields

    with connection.cursor() as cursor2:
        cursor2.execute(query)
        rows = cursor2.fetchall()

        value = []
        for num in range(0, len(fields_chart)):
            value.append([row[num] for row in rows])

        labels = [row[-1] for row in rows]

        if None in labels:
            labels = ['Non assegnato' if v is None else v for v in labels]

        for i in range(len(value)):
            for j in range(len(value[i])):
                if value[i][j] is not None:
                    value[i][j] = round(value[i][j], 2)

        context = {
            'value': value,
            'labels': labels,
            'id': id_sql,
            'name': name_chart,
            'fields': fields_chart,
        }

        if layout_chart == 'barchart':
            return render_to_string('other/barchart.html', context, request=request)
        elif layout_chart == 'piechart':
            return render_to_string('other/piechart.html', context, request=request)
        elif layout_chart == 'linechart':
            return render_to_string('other/linechart.html', context, request=request)


@login_required(login_url='/login/')
def record_card_duplicate(request):
    return render(request)


# Questa funzione serve per copiare la path del record
@login_required(login_url='/login/')
def record_card_copy(request):
    link = request.POST.get('link')
    pyperclip.copy(link)

    return True


# Questa funzione serve per elimiare un record in safe mode
@login_required(login_url='/login/')
def get_record_card_delete(request):
    if request.method == 'POST':
        recordid = request.POST.get('recordid')
        tableid = request.POST.get('tableid')

        with connection.cursor() as cursor:
            query = f"UPDATE user_{tableid} SET deleted_ = 'Y' WHERE recordid_= '{recordid}'"
            cursor.execute(
                query
            )
    return JsonResponse({'success': True})


@user_passes_test(lambda u: u.is_superuser)
def get_render_gestione_utenti(request):
    return render(request, 'other/gestione_utenti.html')


# Questa funzione serve per buildare il gantt e ritornarlo in una pagina html (per ora non in utilizzo)
@login_required(login_url='/login/')
def get_block_records_gantt(request):
    context = dict()
    tableid = request.POST.get('tableid')
    post = {
        'table': 'task',
        'searchTerm': '',
    }

    response = requests.post(
        f"{bixdata_server}bixdata/index.php/rest_controller/get_records_gantt", data=post)
    response_dict = json.loads(response.text)

    records = response_dict['records']

    records_gantt = []
    for record in records:
        new_record = dict()
        new_record['id'] = record[1]
        new_record['name'] = record[2]
        new_record['start'] = record[3]
        new_record['end'] = record[4]
        new_record['progress'] = 100

        records_gantt.append(new_record)
    records_json = json.dumps(records_gantt)

    context = {
        'records': records,
        'records_json': records_json,
    }
    records_table = render_to_string(
        'block/records/records_gantt.html', context, request=request)
    return HttpResponse(records_table)


# Questa funzione serve per buildare il kanban e ritornarlo in una pagina html (per ora non in utilizzo)
@login_required(login_url='/login/')
def get_block_records_kanban(request):
    context = dict()
    tableid = request.POST.get('tableid')
    post = {
        'table': 'deal',
        'searchTerm': '',
    }

    # response = requests.post("http://10.0.0.133:8822/bixdata/index.php/rest_controller/get_records_kanban", data=post)
    # response_dict = json.loads(response.text)
    # groups=response_dict['groups']
    # records = response_dict['records']
    groups = []
    # for record in records:
    #   new_record = dict()
    #  new_record['id'] = record[1]
    # new_record['name'] = record[2]
    # new_record['start'] = record[3]
    # new_record['end'] = record[4]
    # new_record['progress'] = 100
    #    records_kanban.append(new_record)

    group = dict()
    group['description'] = 'TODO test'
    group_records = []
    record = dict()
    record['recordid'] = '123456789'
    record['title'] = 'title'
    record['tag'] = 'tag'
    record['date'] = 'date'
    record['user'] = 'user'
    record['field1'] = 'field1'
    record['field2'] = 'field2'
    record['field3'] = 'field3'
    record['field4'] = 'field4'
    group_records.append(record)
    group['records'] = group_records
    groups.append(group)

    group = dict()
    group['description'] = 'IN PROGRESS'
    group_records = []
    record = dict()
    record['recordid'] = '2222344453'
    record['title'] = 'title2'
    record['tag'] = 'tag2'
    record['date'] = 'date2'
    record['user'] = 'user2'
    record['field1'] = 'field12'
    record['field2'] = 'field22'
    record['field3'] = 'field32'
    record['field4'] = 'field42'
    group_records.append(record)
    group['records'] = group_records
    groups.append(group)

    context = {
        'groups': groups,
        'tableid': tableid,
    }
    records_table = render_to_string(
        'block/records/records_kanban.html', context, request=request)
    return HttpResponse(records_table)


@login_required(login_url='/login/')
def get_block_records_calendar(request):

    oc = OfficeCalendar()
    events = oc.get_calendar_events()


    return render(request, 'block/records/records_calendar.html', {'events': events})


# Questa funzione
@login_required(login_url='/login/')
def get_block_record(request):
    table = request.POST.get('table')
    searchTerm = request.POST.get('searchTerm')
    viewid = request.POST.get('viewid')
    post = {
        'table': table,
        'searchTerm': searchTerm,
        'viewid': viewid,
    }
    response = requests.post(
        f"{bixdata_server}bixdata/index.php/rest_controller/get_records", data=post)
    response_dict = json.loads(response.text)
    columns = response_dict['columns']
    records = response_dict['records']
    context = {
        'records': records,
        'columns': columns,
        'tableid': table,
    }

    for records_index, record in enumerate(records):
        for record_index, value in enumerate(record):
            if record_index == 4:
                # record[index]=split(value)
                value = value.split('|:|')
                record[record_index] = value[0]
            else:
                record[record_index] = value
        records[records_index] = record

    records_table = render_to_string(
        'block/records_table.html', context, request=request)
    return records_table


# Questa funzione richiama la funzione per creare la record card e ritorna la card come http response
@login_required(login_url='/login/')
def request_block_record_card(request):
    tableid = request.POST.get('tableid')
    recordid = request.POST.get('recordid')
    userid = request.user.id
    return HttpResponse(get_block_record_card(tableid, recordid, userid))


# Questa funzione serve per creare la record card e ritorna la card come stringa
def get_block_record_card(tableid, recordid, userid):
    context = dict()
    context['block_record_badge'] = get_block_record_badge(tableid, recordid)
    context['block_record_linked'] = get_block_record_linked(tableid, recordid)
    context['block_record_fields'] = ""
    context['recordid'] = recordid
    context['tableid'] = tableid
    if tableid == 'ticket':
        with connection.cursor() as cursor:
            cursor.execute(f"SELECT freshdeskid FROM user_ticket WHERE recordid_={recordid}")
            freshdeskid = cursor.fetchone()[0]
            context['freshdeskid'] = freshdeskid
    context['userid'] = userid
    context['user_table_settings'] = get_user_table_settings(userid, tableid)
    # returned = user_agent(request, 'block/record/record_card.html', 'block/record/record_card_mobile.html', context)
    return render_to_string('block/record/record_card.html', context)


# Questa funzione richiama la funzione per creare il badge e lo ritorna
@login_required(login_url='/login/')
def request_block_record_badge(request, http_response=False):
    tableid = request.POST.get('tableid')
    recordid = request.POST.get('recordid')
    return get_block_record_badge(tableid, recordid)


# Questa funzione serve per creare il badge
def get_block_record_badge(tableid, recordid):
    context = dict()

    post = {
        'tableid': tableid,
        'recordid': recordid,
    }
    # response = requests.post("http://10.0.0.133:8822/bixdata/index.php/rest_controller/get_fissi", data=post)
    # response_dict = json.loads(response.text)
    sql = f"SELECT sys_field.* FROM sys_field join sys_user_order on sys_field.fieldid=sys_user_order.fieldid WHERE sys_user_order.userid=1 AND sys_user_order.tableid='{tableid}' AND typePreference='campiFissi' ORDER BY fieldorder asc"

    fields = db_query_sql(sql)
    values = db_get_row(f"user_{tableid}", "*", f"recordid_='{recordid}'")
    context_fields = dict()
    for field in fields:
        fieldid = field['fieldid']
        field['value'] = values[fieldid]
        context_fields[fieldid] = field

    context['fields'] = context_fields

    records_table = ""

    if tableid == 'company':
        sql = f"SELECT DISTINCT type FROM user_servicecontract WHERE recordidcompany_='{recordid}' AND STATUS='In Progress'"
        context_fields['services'] = db_query_sql(sql)
        context['fields'] = context_fields
        records_table = render_to_string('block/record/custom/record_badge_company.html', context)

    # elif tableid == 'project':
    #    records_table = render_to_string('block/record/custom/record_badge_project.html', context)

    # else:
    # render_to_string('block/record/record_badge.html', context)

    return records_table


@login_required(login_url='/login/s')
def get_block_record_fields(request):
    context = dict()
    http_response = request.POST.get('http_response')
    tableid = request.POST.get('tableid')
    recordid = request.POST.get('recordid')
    ticketid = request.POST.get('ticketid')
    recordid_ticket = request.POST.get('recordid_ticket')
    master_tableid = request.POST.get('master_tableid')
    master_recordid = request.POST.get('master_recordid')
    contextfunction = request.POST.get('contextfunction')
    contextreference = request.POST.get('contextreference')
    # creator = request.POST.get('creator')

    row = SysUser.objects.filter(bixid=request.user.id).values('id')

    if row:
        userid = row[0]
        userid = userid['id']
    post = {
        'tableid': tableid,
        'recordid': recordid,
        'master_tableid': master_tableid,
        'master_recordid': master_recordid,
        'userid': userid
    }


    response = requests.post(
        f"{bixdata_server}bixdata/index.php/rest_controller/get_record_fields", data=post)

    response_dict = json.loads(response.text)

    if (ticketid):
        response_dict['Dati']['_recordidticket']['valuecode'][0]['value'] = ticketid
        response_dict['Dati']['_recordidticket']['valuecode'][0]['code'] = recordid_ticket

    if tableid == 'timetracking':
        start = response_dict['Dati']['start']['valuecode'][0]['value']

        if start == '':
            response_dict['Dati']['start']['value'] = datetime.datetime.now().strftime("%H:%M")

    context['record_fields_labels'] = response_dict
    context['contextfunction'] = contextfunction
    context['contextreference'] = contextreference
    context['tableid'] = tableid
    context['recordid'] = recordid
    context['master_tableid'] = master_tableid
    context['master_recordid'] = master_recordid

    if tableid == 'timesheet':
        context['timesheet'] = uuid.uuid4()
        context['block_record_fields'] = render_to_string('block/record/record_fields.html', context, request=request)
        block_record_fields = render_to_string('block/record/custom/record_fields_timesheet.html', context,
                                               request=request)
    else:
        context['block_record_fields'] = render_to_string('block/record/record_fields.html', context, request=request)
        block_record_fields = render_to_string('block/record/record_fields_container.html', context, request=request)

    if (http_response):
        return HttpResponse(block_record_fields)
    else:
        return block_record_fields


@login_required(login_url='/login/')
def get_block_record_linked_OLD(request):
    context = dict()
    tableid = request.POST.get('tableid')
    recordid = request.POST.get('recordid')
    post = {
        'tableid': tableid,
        'recordid': recordid,
    }
    response = requests.post(
        f"{bixdata_server}bixdata/index.php/rest_controller/get_record_labels", data=post)
    response_dict = json.loads(response.text)
    context['labels'] = response_dict
    context['tableid'] = tableid
    context['recordid'] = recordid
    record_linked_labels = render_to_string(
        'block/record/record_linked.html', context, request=request)
    return record_linked_labels


@login_required(login_url='/login/')
def request_block_record_linked(request):
    tableid = request.POST.get('tableid')
    recordid = request.POST.get('recordid')
    return HttpResponse(get_block_record_linked(tableid, recordid))


def get_block_record_linked(tableid, recordid):
    context = dict()

    rows = db_query_sql(
        f"SELECT sys_table_link.*,typepreference,sys_user_order.ID FROM sys_table_link JOIN sys_user_order ON sys_table_link.tableid=sys_user_order.tableid AND sys_table_link.tablelinkid=sys_user_order.fieldid  WHERE sys_table_link.tableid = '{tableid}' AND typepreference='keylabel'")

    linked_tables = list()
    for row in rows:
        linked_table = dict()
        linked_tableid = row['tablelinkid']
        table_name = 'test'
        linked_table['table_name'] = db_get_value("sys_table", "description", f"id='{linked_tableid}'")
        table_count = db_get_count(f"user_{linked_tableid}", f"recordid{tableid}_='{recordid}'")
        linked_table['table_count'] = table_count
        linked_table['tableid'] = linked_tableid
        linked_tables.append(linked_table)

    context['linked_tables'] = linked_tables
    context['tableid'] = tableid
    context['recordid'] = recordid

    record_linked_labels = render_to_string('block/record/record_linked.html', context)
    return record_linked_labels


@login_required(login_url='/login/')
def get_linked(request):
    name = ''
    if request.method == 'POST':
        name = request.POST.get('name')
    return JsonResponse(name)


@login_required(login_url='/login/')
def save_record_fields(request):
    tableid = request.POST.get('tableid')
    recordid = request.POST.get('recordid')
    fields = request.POST.get('fields')
    fields_dict = json.loads(fields)
    contextfunction = request.POST.get('contextfunction')

    if tableid == 'timetracking':
        if fields_dict['stato'] == 'Terminato':
            if fields_dict['end'] == '':
                fields_dict['end'] = datetime.datetime.now().strftime("%H:%M")
            time_format = '%H:%M'
            start = datetime.datetime.strptime(fields_dict['start'], time_format)
            end = datetime.datetime.strptime(fields_dict['end'], time_format)
            time_difference = end - start

            hours = time_difference.total_seconds() / 3600
            fields_dict['worktime'] = round(hours, 2)

    selected_options = request.POST.getlist('service');

    if tableid == 'task':
        oc = OfficeCalendar()
        if fields_dict['planneddate'] != '':
            if fields_dict['o365_idcalendar'] == '':
                fields_dict['o365_idcalendar'] = oc.add_calendar_event(fields_dict)
            else:
                oc.update_calendar_event(fields_dict)

    fields = json.dumps(fields_dict)

    post_data = {
        'tableid': tableid,
        'recordid': recordid,
        'fields': fields
    }

    response = requests.post(
        f"{bixdata_server}bixdata/index.php/rest_controller/set_record", data=post_data)



    if contextfunction == 'edit':
        if tableid == 'task':
            check_task_status(recordid)

    if contextfunction == 'insert':
        if tableid == 'ticketbixdata' and 'description' in fields_dict:
            message = 'Nuovo ticket aperto da {} \nDescrizione: {}\nTipo: {}'.format(request.user.username,
                                                                                     fields_dict['description'],
                                                                                     fields_dict.get('type', 'N/A'))
            send_email(emails=['marco.garganigo@swissbix.ch', 'alessandro.galli@swissbix.ch'],
                       subject='Supporto bixdata', html_message=message)

        elif tableid == 'task':

            if fields_dict['user'] != fields_dict['creator']:
                with connection.cursor() as cursor:
                    cursor.execute("SELECT email FROM v_users WHERE sys_user_id = %s", [fields_dict['user']])
                    row = cursor.fetchone()

                    email = row[0]

                    cursor.execute("SELECT first_name, last_name FROM v_users WHERE sys_user_id = %s",
                                   [fields_dict['creator']])
                    row = cursor.fetchone()
                    first_name = row[0]
                    last_name = row[1]

                    companyname = 'N/A'
                    projectname = 'N/A'

                    if fields_dict['recordidcompany_'] != 'None':
                        with connection.cursor() as cursor:
                            cursor.execute("SELECT companyname FROM user_company WHERE recordid_ = %s",
                                           [fields_dict['recordidcompany_']])
                            row = cursor.fetchone()
                            companyname = row[0]

                    if fields_dict['recordidproject_'] != 'None':
                        with connection.cursor() as cursor:
                            cursor.execute("SELECT projectname FROM user_project WHERE recordid_ = %s",
                                           [fields_dict['recordidproject_']])
                            row = cursor.fetchone()
                            projectname = row[0]

                    fields_dict['username'] = first_name + ' ' + last_name
                    fields_dict['companyname'] = companyname
                    fields_dict['projectname'] = projectname

                    message = render_to_string('other/new_task.html', fields_dict)

                    # return render(request, 'other/new_task.html', fields_dict)

                    send_email(emails=[email], subject='Nuovo task assegnato', html_message=message)

    return render(request, 'block/record/record_fields.html')


@login_required(login_url='/login/')
def pagination(request):
    if request.method == 'POST':
        page = request.POST.get('page')
        offset = 50 * page
        # "SELECT * FROM bixdata.user_invoice LIMIT 50 OFFSET %s;", [offset]

    return JsonResponse(page)


def get_test_calendar(request):
    return render(request, 'other/testCalendar.html')


@login_required(login_url='/login/')
def get_temp(request):
    return HttpResponse('test')


@login_required(login_url='/login/')
def get_settings(request):
    settings_list = get_user_setting_list(request)

    return render(request, 'other/settings.html', {'settings_list': settings_list})


@login_required(login_url='/login/')
def get_under_construction(request):
    return render(request, 'other/under_construction.html')


@login_required(login_url='/login/')
def support(request):
    if request.method == 'POST':
        category = request.POST['category']
        description = request.POST['description']
        user = request.user.first_name + ' ' + request.user.last_name

        # Get the uploaded files
        images = request.FILES.getlist('images')

        # Create a directory to store the images
        directory = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'support_images')
        if not os.path.exists(directory):
            os.makedirs(directory)

        # Print the names of the images
        for image in images:
            print(image.name)

        # Do something with the saved images
        # ...

        print(category)
        print(description)
        print(user)
        print(images)

    return redirect('index')


@login_required(login_url='/login/')
def save_settings(request):
    id = None

    row = SysUser.objects.filter(bixid=request.user.id).values('id').first()

    if row:
        id = row['id']

    if request.method == 'POST':
        layout = request.POST.get('record_open_layout')
        theme = request.POST.get('theme')
        active_panel = request.POST.get('active_panel')

        with connection.cursor() as cursor:
            cursor.execute(
                "UPDATE v_sys_user_settings SET value = %s WHERE userid = %s AND setting = 'record_open_layout'",
                [layout, id]
            )
            cursor.execute(
                "UPDATE v_sys_user_settings SET value = %s WHERE userid = %s AND setting = 'theme'",
                [theme, id]
            )
            cursor.execute(
                "UPDATE v_sys_user_settings SET value = %s WHERE userid = %s AND setting = 'active_panel'",
                [active_panel, id]
            )

    return redirect('index')


@login_required(login_url='/login/')
def get_account(request):
    user = request.user
    context = {
        'user': user
    }

    return render(request, 'other/account.html', context)


@login_required(login_url='/login/')
def update_profile_pic(request):
    if request.method == 'POST':
        image = request.FILES.get('image')
        if image:
            # Save the uploaded image with the user's username as the filename
            filename = f"{request.user.username}.png"
            filepath = os.path.join(settings.MEDIA_ROOT, filename)
            with open(filepath, 'wb') as f:
                for chunk in image.chunks():
                    f.write(chunk)
            # Update the user's profile image URL in the database

    return redirect('index')


@login_required(login_url='/login/')
def admin_page(request):
    page = request.POST.get('page')

    rows = SysUserDashboard.objects.all().values()

    userids = [row['userid'] for row in rows]
    dashboardids = [row['dashboardid'] for row in rows]

    rows2 = SysUser.objects.filter(id__in=userids).values('firstname', 'lastname')

    names = [row['firstname'] + ' ' + row['lastname'] for row in rows2]

    rows4 = SysView.objects.all().values()
    rows5 = SysReport.objects.all().values()
    tables = SysTable.objects.all().values('id')
    fields = SysField.objects.all().values('tableid', 'fieldid')

    with connection.cursor() as cursor3:
        cursor3.execute(
            "SELECT * FROM v_sys_dashboard_block"
        )
        rows3 = dictfetchall(cursor3)

        chart_names = [row['name'] for row in rows3]
        chart_dashboard_id = [row['dashboardid'] for row in rows3]

    context = {
        'userids': userids,
        'dashboardids': dashboardids,
        'names': names,
        'chart_names': chart_names,
        'chart_dashboard_id': chart_dashboard_id,
        'views': rows4,
        'reports': rows5,
        'tables': tables,
        'fields': fields,

    }

    return render(request, f'admin_settings/{page}.html', {'context': context})


@login_required(login_url='/login/')
def save_chart_settings(request):
    if request.method == 'POST':
        userids = request.POST.getlist('userids[]')
        dashboardids = request.POST.getlist('dashboardids[]')
        names = request.POST.getlist('chartnames[]')
        chartdashboardids = request.POST.getlist('chartdashboardids[]')

        for i in range(len(userids)):
            user_id = userids[i]
            dashboard_id = dashboardids[i]
            SysUserDashboard.objects.filter(userid=user_id).update(dashboardid=dashboard_id)

        with connection.cursor() as cursor:
            for i in range(len(names)):
                name = names[i]
                dashboard_id = chartdashboardids[i]

                cursor.execute('UPDATE v_sys_dashboard_block SET dashboardid = %s WHERE name = %s',
                               [dashboard_id, name])

    return redirect('index')


@login_required(login_url='/login/')
def new_chart_block(request):
    if request.method == 'POST':
        name = request.POST.get('block_name')
        dashboard_id = request.POST.get('dashboard_id')
        view_id = request.POST.get('view_id')
        report_id = request.POST.get('report_id')

        SysDashboardBlock.objects.create(
            dashboardid=dashboard_id,
            name=name,
            userid=1,
            viewid=view_id,
            reportid=report_id
        )

    return redirect('index')


@login_required(login_url='/login/')
def get_record_path(request, tableid, recordid):
    userid = request.user.id
    if tableid == 'timesheet':
        content = get_block_timesheetinvoice(recordid, userid)
    elif tableid == 'task':
        content = get_block_task(recordid, userid)
    elif tableid == 'ticket':
        content = insert_timesheet(request, recordid, userid)
    return get_render_index(request, content)


def insert_timesheet(request, ticketid, userid):
    with connection.cursor() as cursor:
        cursor.execute(
            f"SELECT recordid_, email FROM user_ticket WHERE freshdeskid = '{ticketid}'"
        )
        rows = dictfetchall(cursor)
        recordid_ticket = rows[0]['recordid_']
        email = rows[0]['email']

    tableid = 'timesheet'
    contextfunction = 'insert'
    contextreference = tableid
    http_response = 'true'
    called_from = 'url'
    recordid = None

    table_block = get_records_table(request, 'company', None, None, email, '', 1, '', '')

    ticket_block = get_block_record_card('ticket', recordid_ticket, userid)
    # timesheet_block = get_block_record_fields(request, tableid, contextfunction, contextreference, recordid, userid, http_response, called_from)

    data = {
        'ticketid': ticketid,
        'recordid_ticket': recordid_ticket,
        'ticket_block': ticket_block,
        'table_block': table_block,
        'contextfunction': contextfunction,
        'tableid': tableid,
        'recordid': recordid,
        'userid': userid,
        'http_response': http_response,

    }

    content = render_to_string('other/insert_timesheet.html', data)

    return content


def get_block_task(recordid_task, userid):
    with connection.cursor() as cursor:
        cursor.execute(
            f"SELECT * FROM user_task WHERE recordid_='{recordid_task}'"
        )
        rows = dictfetchall(cursor)
    if (rows):
        context = dict()
        context['task'] = rows[0]
        context['task_block'] = get_block_record_card('task', recordid_task, userid)
        content = render_to_string('other/check_task.html', context)
        return content
    else:
        return ''


def get_block_timesheetinvoice(recordid_timesheet, userid):
    timesheet_block = get_block_record_card('timesheet', recordid_timesheet, userid)
    company_block = ''
    project_block = ''
    with connection.cursor() as cursor:
        cursor.execute(
            f"SELECT * FROM user_timesheet WHERE recordid_='{recordid_timesheet}'"
        )
        rows = dictfetchall(cursor)
    if (rows):
        recordid_company = rows[0]['recordidcompany_'];
        company_block = get_block_record_card('company', recordid_company, userid)

    context = dict()
    context['timesheet_block'] = timesheet_block
    context['company_block'] = company_block
    content = render_to_string('other/check_timesheetinvoice.html', context)
    return content;


@login_required(login_url='/login/')
def get_badge(request):
    return True


@login_required(login_url='/login/')
def get_timesheet_serviceassets(request):
    return HttpResponse('test')


@login_required(login_url='/login/')
def get_bixdata_updates(request):
    user_id = request.user.id
    return render(request, 'other/bixdata_updates.html', {'user_id': user_id})


@login_required(login_url='/login/')
def new_update(request):
    return render(request, 'other/bixdata_updates.html')


def stampa_timesheet(request):
    recordid = ''
    if request.method == 'POST':
        recordid = request.POST.get('recordid')
        filename = request.POST.get('filename')

        with connection.cursor() as cursor:
            cursor.execute(
                f"SELECT   t.*,c.companyname,c.address,c.city,c.email,u.firstname, u.lastname FROM user_timesheet as t join user_company as c on t.recordidcompany_=c.recordid_ join sys_user as u on t.user = u.id WHERE t.recordid_='{recordid}'"
            )
            rows = dictfetchall(cursor)

            row = rows[0]
            row['recordid'] = recordid

        script_dir = os.path.dirname(os.path.abspath(__file__))
        wkhtmltopdf_path = script_dir + '\\wkhtmltopdf.exe'

        config = pdfkit.configuration(wkhtmltopdf=wkhtmltopdf_path)
        content = render_to_string('pdf/timesheet.html', row)
        pdfkit.from_string(content, filename, configuration=config)

        # Open the file and read its contents
        with open(filename, 'rb') as file:
            file_data = file.read()
            file_data = file.read()

        # Delete the file from the file system
        # os.remove(filename)

        # Create an HTTP response with the file contents
        response = HttpResponse(file_data, content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="{filename}"'
        return response


def stampa_servicecontract(request):
    recordid = ''
    if request.method == 'POST':
        recordid = request.POST.get('recordid')
        filename = request.POST.get('filename')

        with connection.cursor() as cursor:
            cursor.execute(
                f"SELECT s.*,c.companyname,c.address,c.city,c.email FROM user_servicecontract as s join user_company as c on s.recordidcompany_=c.recordid_  WHERE s.recordid_='{recordid}'"
            )
            rows = dictfetchall(cursor)

            row = rows[0]
            row['recordid'] = recordid
            row['date'] = datetime.datetime.now().strftime("%d/%m/%Y")

        script_dir = os.path.dirname(os.path.abspath(__file__))
        wkhtmltopdf_path = script_dir + '\\wkhtmltopdf.exe'

        context = row
        with connection.cursor() as cursor:
            cursor.execute(
                f"SELECT t.*,u.firstname,u.lastname FROM user_timesheet as t join sys_user as u on t.user=u.id  WHERE t.recordidservicecontract_='{recordid}'"
            )
            timesheets = dictfetchall(cursor)
        context['timesheets'] = timesheets

        config = pdfkit.configuration(wkhtmltopdf=wkhtmltopdf_path)
        content = render_to_string('pdf/servicecontract.html', row)

        filename_with_path = os.path.join('bixdata_app/static/pdf', filename)
        filename_with_path = os.path.abspath(filename_with_path)

        pdfkit.from_string(content, filename_with_path, configuration=config)

        # Open the file and read its contents
        with open(filename_with_path, 'rb') as file:
            file_data = file.read()

        # Delete the file from the file system
        # os.remove(filename_with_path)

        # Create an HTTP response with the file contents
        response = HttpResponse(file_data, content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="{filename}"'
        return response


def stampa_servicecontract_test(request):
    recordid = request.POST.get('recordid')
    filename = request.POST.get('filename')

    with connection.cursor() as cursor:
        cursor.execute(
            f"SELECT s.*,c.companyname,c.address,c.city,c.email FROM user_servicecontract as s join user_company as c on s.recordidcompany_=c.recordid_  WHERE s.recordid_='{recordid}'"
        )
        rows = dictfetchall(cursor)

        row = rows[0]
        row['recordid'] = recordid
        row['date'] = datetime.datetime.now().strftime("%d/%m/%Y")

    context = row
    with connection.cursor() as cursor:
        cursor.execute(
            f"SELECT t.*,u.firstname,u.lastname FROM user_timesheet as t join sys_user as u on t.user=u.id  WHERE t.recordidservicecontract_='{recordid}'"
        )
        timesheets = dictfetchall(cursor)
    context['timesheets'] = timesheets

    return render(request, 'pdf/servicecontract.html', context)


def new_ticket_timesheet(request, ticket):
    userid = request.user.id
    content = get_block_ticket_timesheet(request, ticket, userid)
    return get_render_index(request, content)


def get_block_ticket_timesheet(request, ticket, userid):
    with connection.cursor() as cursor:
        cursor.execute(
            f"SELECT * FROM user_ticket WHERE freshdeskid='{ticket}'"
        )
        rows = dictfetchall(cursor)
        if rows:
            recordid = rows[0]['recordid_']
            ticket_block = get_block_record_card('ticket', recordid, userid)

            context = dict()
            context['ticket_block'] = ticket_block
            content = render_to_string('other/check_ticket.html', context)

        return content


def rinnova_contratto(request):
    recordid = request.POST.get('recordid')
    contract_hours = request.POST.get('contract_hours')
    invoicenr = request.POST.get('invoicenr')

    post_data = {
        'recordid': recordid,
        'contracthours': contract_hours,
        'invoiceno': invoicenr,
        'startdate': datetime.datetime.now().strftime("%Y-%m-%d")
    }
    response = requests.post(f"{bixdata_server}bixdata/index.php/rest_controller/rinnova_contratto", data=post_data)
    return HttpResponse('ok')


def sort_records(request):
    tableid = request.POST.get('tableid')
    order = request.POST.get('order')
    column_name = request.POST.get('order_field')

    if order == 'asc':
        icon = 'mdi mdi-arrow-down-thin'
    else:
        icon = 'mdi mdi-arrow-up-thin'

    return icon


def export_excel(request):
    tableid = request.POST.get('tableid')
    master_tableid = request.POST.get('master_tableid')
    master_recordid = request.POST.get('master_recordid')
    searchTerm = request.POST.get('searchTerm')
    viewid = request.POST.get('viewid')
    order_field = request.POST.get('order_field')
    order = request.POST.get('order')
    # currentpage = request.POST.get('currentpage')
    currentpage = 0

    post = {
        'tableid': tableid,
        'searchTerm': searchTerm,
        'viewid': viewid,
        'currentpage': currentpage,
        'order_field': order_field,
        'order': order,
        'master_tableid': master_tableid,
        'master_recordid': master_recordid,
        'userid': request.user.id
    }
    response = requests.post(f"{bixdata_server}bixdata/index.php/rest_controller/get_records", data=post)
    response_dict = json.loads(response.text)

    csv_file = tableid + '-' + uuid.uuid4().hex + '.csv'

    csv_columns = []
    for count, col in enumerate(response_dict['columns']):
        if count > 2:
            csv_columns.append(col['desc'])

    # records = [row[3:] for row in response_dict['records']]

    records = []
    for response_dict_record in response_dict['records']:
        record = []
        for response_dict_record_field in response_dict_record[3:]:
            record.append(remove_html_tags(response_dict_record_field))
        records.append(record)

    with open(csv_file, 'w', newline='', encoding='utf-8-sig') as file:
        writer = csv.writer(file, delimiter=';')

        writer.writerow(csv_columns)
        writer.writerows(records)

    with open(csv_file, 'rb') as file:
        response = HttpResponse(file.read(), content_type='text/csv')
        response['Content-Disposition'] = 'attachment'
        response['filename'] = csv_file

    os.remove(csv_file)

    return response


def get_records_grouped(request):
    tableid = request.POST.get('tableid')
    table_name = 'user_' + tableid

    with connection.cursor() as cursor:
        cursor.execute(
            f"SELECT c.companyname, COUNT(c.recordid_) AS NumeroTask, t.* FROM {table_name} AS t LEFT JOIN user_company AS c ON t.recordidcompany_ = c.recordid_ GROUP BY c.companyname"
        )
        rows = dictfetchall(cursor)

    context = dict()
    context['rows'] = rows

    return render(request, 'block/records/records_grouped.html', context)


# @user_passes_test(lambda u: u.is_superuser)
def send_active_task(request, requested_user=''):
    if requested_user != '':
        userid = requested_user

        with connection.cursor() as cursor:
            cursor.execute(
                "SELECT * from v_users where id = %s", [userid]
            )
            users = dictfetchall(cursor)
    else:
        with connection.cursor() as cursor:
            cursor.execute(
                "SELECT * from v_users where is_active=1"
            )
            users = dictfetchall(cursor)

    for user in users:
        sys_user_id = user['sys_user_id']
        with connection.cursor() as cursor:
            cursor.execute(
                f"SELECT user_task.*, v_users.username, user_company.companyname FROM user_task LEFT JOIN v_users ON user_task.creator = v_users.sys_user_id LEFT JOIN user_company on user_task.recordidcompany_ = user_company.recordid_ WHERE user={sys_user_id} and user_task.status!='Chiuso' and user_task.deleted_ = 'N'"
            )
            tasks = dictfetchall(cursor)

            cursor.execute(
                f"SELECT user_task.*, v_users.username, user_company.companyname FROM user_task LEFT JOIN v_users ON user_task.user = v_users.sys_user_id LEFT JOIN user_company on user_task.recordidcompany_ = user_company.recordid_ WHERE creator={sys_user_id} and user != {sys_user_id} and user_task.status!='Chiuso' and user_task.deleted_ = 'N' "
            )
            tasks_created = dictfetchall(cursor)

            current_date = datetime.date.today()
            one_week_ago = current_date - datetime.timedelta(days=7)

            # Format the date range in the YYYY-MM-DD format
            current_date_str = current_date.strftime("%Y-%m-%d")
            one_week_ago_str = one_week_ago.strftime("%Y-%m-%d")

            query = f"SELECT user_task.*, v_users.username, user_company.companyname FROM user_task \
                         LEFT JOIN v_users ON user_task.user = v_users.sys_user_id \
                         LEFT JOIN user_company ON user_task.recordidcompany_ = user_company.recordid_ \
                         WHERE creator={sys_user_id} AND user != {sys_user_id} \
                         AND closedate >= '{one_week_ago_str}' AND closedate <= '{current_date_str}' AND user_task.completed = 'Si' AND user_task.deleted_ = 'N'"

            cursor.execute(
                query
            )

            tasks_completed = dictfetchall(cursor)

            if tasks or tasks_created or tasks_completed:
                html_message = ""
                context = dict()
                for task in tasks:
                    if task['creator'] is not None:
                        task['creator'] = task['creator']
                    else:
                        task['creator'] = 'N/A'

                context['data'] = tasks
                context['data_created'] = tasks_created
                context['tasks_completed'] = tasks_completed
                html_message = render_to_string('other/send_active_task.html', context)

                subject = f"Report task - {user['first_name']} {user['last_name']}"
                email = user['email']
                send_email(emails=[email], subject=subject, html_message=html_message)

    return HttpResponse('ok')


def send_unique_active_task(request):
    requested_user = request.user.id
    send_active_task(request, requested_user)

    return True


def update_task_status(request):
    with connection.cursor() as cursor:
        cursor.execute(
            f"SELECT * from user_task"
        )
        tasks = dictfetchall(cursor)

        current_date = datetime.date.today()
        current_date_str = current_date.strftime("%Y-%m-%d")

        for task in tasks:
            if task['closedate'] < current_date_str:
                cursor.execute(
                    f"UPDATE user_task SET status = 'Scaduto' WHERE recordid_ = {task['recordid_']}"
                )

            elif current_date_str < task['closedate'] < current_date_str + datetime.timedelta(days=2):
                cursor.execute(
                    f"UPDATE user_task SET status = 'In scadenza' WHERE recordid_ = {task['recordid_']}"
                )
            else:
                cursor.execute(
                    f"UPDATE user_task SET status = 'Aperto' WHERE recordid_ = {task['recordid_']}"
                )

    return HttpResponse('ok')


def update_task_status(request):
    with connection.cursor() as cursor:
        cursor.execute(
            f"SELECT * from user_task where status!='Chiuso'"
        )
        tasks = dictfetchall(cursor)
    for task in tasks:
        post_data = {
            'tableid': 'task',
            'recordid': task['recordid_'],
            'fields': []
        }

        response = requests.post(f"{bixdata_server}bixdata/index.php/rest_controller/set_record", data=post_data)
    return HttpResponse('Eseguito')


def validate_timesheet(request):
    recordid = request.POST.get('recordid')

    with connection.cursor() as cursor:
        cursor.execute(
            "UPDATE user_timesheet SET validated = 'Si' WHERE recordid_ = %s", [recordid]
        )

    return HttpResponse('done')


def check_task_status(recordid):
    with connection.cursor() as cursor2:
        cursor2.execute(
            "SELECT * FROM user_task WHERE user_task.user != creator AND recordid_ = %s",
            [recordid]
        )
        task = dictfetchall(cursor2)
        if task:
            user = task[0]['user']
            company = task[0]['recordidcompany_']
        else:
            return HttpResponse('ok')

        cursor2.execute(
            "SELECT first_name, last_name   FROM v_users WHERE sys_user_id = %s",
            [user]
        )
        user = dictfetchall(cursor2)
        username = user[0]['first_name'] + ' ' + user[0]['last_name']

        cursor2.execute(
            "SELECT companyname FROM user_company WHERE recordid_ = %s",
            [company]
        )
        company = dictfetchall(cursor2)
        company = company[0]['companyname']

    if task and 'status' in task[0]:
        status = task[0]['status']
        if status == 'Chiuso':
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT description, email, username FROM v_users INNER JOIN user_task "
                    "ON v_users.sys_user_id = user_task.creator WHERE user_task.recordid_ = %s",
                    [recordid]
                )
                user = dictfetchall(cursor)

            if user:
                email = user[0]['email']
                description = user[0]['description']

                message = render_to_string('other/close_task.html',
                                           {'username': username, 'company': company, 'description': description})
                send_email(
                    emails=[email],
                    subject='Task chiuso',
                    html_message=message
                )

    return HttpResponse('ok')


def staff_only(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):

        if request.user.is_staff:
            return view_func(request, *args, **kwargs)
        else:
            return HttpResponse('Non sei autorizzato ad accedere a questa pagina')

    return wrapper

def check_mails():
    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT * from user_task where status = 'Errore'"
        )
        tasks = dictfetchall(cursor)

    return True

def test_gridstack(request):
    return render(request, 'other/test_gridstack.html')


def new_block(request):
    blockid = request.POST.get('blockid')
    userid = request.POST.get('userid')

    SysUserDashboardBlock.objects.create(
        userid=userid,
        dashboard_block_id=blockid
    )

    return JsonResponse({'success': True})


def remove_block(request):
    blockid = request.POST.get('blockid')
    SysUserDashboardBlock.objects.filter(id=blockid).delete()

    return JsonResponse({'success': True})


def new_report(request):
    tableid = request.POST.get('tableid')
    report_name = request.POST.get('report_name')
    fieldid = request.POST.get('fieldid')
    operation = request.POST.get('operation')
    layout = request.POST.get('layout')
    groupby = request.POST.get('groupby')
    SysReport.objects.create(
        userid=1,
        tableid=tableid,
        name=report_name,
        fieldid=fieldid,
        operation=operation,
        layout=layout,
        groupby=groupby
    )

    return JsonResponse({'success': True})


def test_select(request):
    return render(request, 'other/test.html')


def order_settings(request):
    tables = SysTable.objects.all().values('id')

    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT * FROM v_users WHERE is_active = 1"
        )
        users = dictfetchall(cursor)

    return render(request, 'other/order_settings.html', {'tables': tables, 'users': users})


def get_table_fields(request):
    if request.method == 'POST':
        tableid = request.POST.get('tableid')
        typepreference = request.POST.get('type')
        with connection.cursor() as cursor:
            cursor.execute(

                f"SELECT sys_field.*,sys_user_order.fieldorder,sys_user_order.id AS fieldid_real FROM sys_field LEFT JOIN  (SELECT * FROM sys_user_order WHERE typepreference = '{typepreference}' ) AS sys_user_order ON sys_field.fieldid = sys_user_order.fieldid  AND sys_field.tableid = sys_user_order.tableid WHERE  sys_field.tableid = '{tableid}'"

            )
            fields = dictfetchall(cursor)

            for field in fields:
                if field['fieldid_real'] is None:
                    field['fieldid_real'] = 'None'

            returned = render_to_string('other/settings_fields.html', {'fields': fields})

            return HttpResponse(returned)


def save_fields_order(request):
    if request.method == 'POST':
        tableid = request.POST.get('tableid')
        fields_json = request.POST.get('fields')
        fields = json.loads(fields_json)

        # with connection.cursor() as cursor:
        # for count, field in enumerate(fields):
        # cursor.execute(
        #   f"UPDATE sys_user_order SET userid = 1, fieldorder = {count} WHERE tableid = '{tableid}' AND fieldid = '{field['id']}'"
        # )

        return JsonResponse({'success': True})


def update_pending_timesheet(request):
    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT * FROM user_timesheet WHERE deleted_ = 'N' AND status = 'To Invoice when Ticket Closed' AND date >= '2023-07-01'"
        )
        timesheets = dictfetchall(cursor)

        for timesheet in timesheets:
            post_data = {
                'tableid': timesheet['tableid'],
                'recordid': timesheet['recordid_'],
            }

            response = requests.post(
                f"{bixdata_server}bixdata/index.php/rest_controller/set_record", data=post_data)

    return HttpResponse('ok')


def get_project_id(request):
    if request.method == 'POST':
        projectid = request.POST.get('projectid')
        print(projectid)
        with connection.cursor() as cursor:
            cursor.execute(
                f"SELECT id, name, quantity FROM user_dealline WHERE recordidproject_ = '{projectid}'"
            )
            rows = dictfetchall(cursor)
            print(rows)

            return JsonResponse({'rows': rows})


def testtest(request):
    return render(request, 'other/test_lock.html')


class Locker:
    def __init__(self):
        self.locks = {}  # Dictionary to store lock information
        self.lock = threading.Lock()  # Create a lock for synchronization

    def acquire_lock(self, recordid, tableid, user):
        lock_key = (recordid, tableid)

        with self.lock:  # Use the lock for thread safety
            # Check if the lock is already acquired
            if lock_key in self.locks:
                return False, self.locks[lock_key]['user'], self.locks[lock_key]['timestamp']

            # If not acquired, create the lock with a timestamp
            timestamp = time.time()
            self.locks[lock_key] = {'user': user, 'timestamp': timestamp}

        return True, None, timestamp

    def release_lock(self, recordid, tableid, user):
        lock_key = (recordid, tableid)

        with self.lock:  # Use the lock for thread safety
            # Check if the lock exists and the user matches
            if lock_key in self.locks:
                if self.locks[lock_key]['user'] == user:
                    del self.locks[lock_key]
                    return True, None

        # Lock doesn't exist or user doesn't match, nothing to release
        return False, None


# Example of how to use the Locker class
locker = Locker()


def test_lock(request):
    if request.method == 'GET':

        recordid = request.GET.get('recordid')
        tableid = request.GET.get('tableid')
        userid = request.user.id  # Replace this with your actual user identification

        with lock:  # Acquire the global lock to ensure only one user at a time
            success, lock_user, timestamp = locker.acquire_lock(recordid, tableid, userid)
            print(lock)

        if success:
            return JsonResponse({'success': True})
        else:

            with connection.cursor() as cursor:
                cursor.execute(
                    f"SELECT username FROM v_users WHERE id = {lock_user}"
                )
                user_inside = cursor.fetchone()[0]

            return JsonResponse({'success': False, 'user': user_inside, 'timestamp': timestamp})

    elif request.method == 'POST':
        recordid = request.POST.get('recordid')
        tableid = request.POST.get('tableid')

        userid = request.user.id  # Replace this with your actual user identification

        with lock:  # Acquire the global lock to ensure only one user at a time
            success = locker.release_lock(recordid, tableid, userid)

        if success:
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False})


# Global lock for ensuring only one user can access the Locker class at a time
lock = threading.Lock()


def admin_table_settings(request):
    tables = SysTable.objects.all().values('id')
    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT * FROM v_users WHERE is_active = 1"
        )
        users = dictfetchall(cursor)

    return render(request, 'other/admin_table_settings.html', {'tables': tables, 'users': users})


def settings_charts(request):
    return render(request, 'admin_settings/settings_charts.html')

def test_adiuto_db(request):
    with connections['adiuto'].cursor() as cursor:
        cursor.execute("SELECT * FROM A1001")
        rows = dictfetchall(cursor)
    return render(request, 'other/test_adiuto_db.html')


def test_admin_doc(request):
    """Esegue una funzione

    Args:
        request (_type_): richiesta d'origin
        function (str): funzione da eseguire

    Returns:
        str: risultato della funzione chiamata, visualizzabile  nel browser
    """
    return HttpResponse('ok')


def get_events_recordid(request):
    events_recordid = []

    events = request.POST.getlist('events')  # Use getlist to get a list of values
    #convert from json to list
    events = json.loads(events[0])

    for event in events:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM user_task WHERE o365_idcalendar = %s", [event])
            event_data = cursor.fetchall()
            events_recordid.append(event_data)

    return JsonResponse({'complete_events': events_recordid})

