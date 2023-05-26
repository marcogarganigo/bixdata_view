import tempfile

import pyperclip
from aiohttp.web_fileresponse import FileResponse
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect
from django.http import JsonResponse
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

from ..forms import LoginForm
from django.contrib.auth.decorators import user_passes_test
from django.contrib import messages
from django.db import connection
from django.http import JsonResponse
from django.contrib.auth.models import Group, Permission, User, Group
from django_user_agents.utils import get_user_agent
from bixdata_app.models import MyModel
from bixdata_app.models import CustomUser
import os
from django.conf import settings
from django.views.decorators.clickjacking import xframe_options_exempt
import subprocess
from .beta import *

bixdata_server = os.environ.get('BIXDATA_SERVER')


def get_test_autocomplete(request):
    return render(request, 'test_autocomplete.html')


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


def get_test_query(request, name=None):
    with connection.cursor() as cursor1:
        cursor1.execute(
            "SELECT query_conditions FROM sys_view WHERE id = 9"
        )
        query = cursor1.fetchone()[0]

        with connection.cursor() as cursor2:
            cursor2.execute(query)
            rows = cursor2.fetchall()

            users = [row[0] for row in rows]
            effective_margins = [row[1] for row in rows]
            expected_margins = [row[2] for row in rows]
            amounts = [row[3] for row in rows]

            data = {
                'users': users,
                'effective_margins': effective_margins,
                'expected_margins': expected_margins,
                'amounts': amounts,
            }

            # Get the custom permission
            permission = Permission.objects.get(codename='can_do_something')

            # Assign the permission to a group
            # group = Group.objects.get(name='My group')
            # group.permissions.add(permission)

            # Assign the permission to a user
            user = User.objects.get(username='test')
            user.user_permissions.add(permission)

            # Check if a user has a permission

    return render(request, 'other/test_query.html', {'data': data})


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


@xframe_options_exempt
@login_required(login_url='/login/')
def get_render_index(request, content=''):
    response = requests.get(
        f"{bixdata_server}bixdata/index.php/rest_controller/get_tables_menu")
    menu_list = json.loads(response.text)

    username = request.user

    # role = username.role
    context = {}

    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT description FROM sys_user WHERE bixid = %s", [request.user.id]
        )
        role = cursor.fetchone()[0]

    theme = get_user_setting(request, 'theme')
    #
    #
    #

    context = {
        'menu_list': menu_list,
        'date': datetime.datetime.now().strftime('%Y-%m-%d-%H:%M:%S'),
        'username': username,
        'role': role,
        'theme': theme,
        'content': content,
        'layout_setting': get_user_setting(request, 'record_open_layout'),
    }

    return user_agent(request, 'index.html', 'index2.html', context)
    # return render(request, 'index.html', context)


def get_render_loading(request):
    return render(request, 'other/loading.html')


# request: {tableid}
@login_required(login_url='/login/')
def get_content_records(request):
    context = dict()
    # records_table = get_block_records_table(request)
    context['records_table'] = ''
    tableid = request.POST.get('tableid')
    context['table'] = tableid.upper()
    context['tableid'] = tableid
    context['views'] = dict()
    context['user_table_settings'] = get_user_table_settings(request.user.id, tableid)
    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT * FROM sys_view WHERE userid = 1 AND tableid='%s'" % (tableid)
        )
        result = dictfetchall(cursor)
        if result:
            context['views'] = result

    layout_setting = get_user_setting(request, 'record_open_layout')
    context['layout_setting'] = layout_setting

    context['loading'] = render_to_string('other/loading.html', context, request)

    #  search fields
    search_fields = dict()
    with connection.cursor() as cursor:
        cursor.execute(
            f"SELECT f.* FROM sys_user_table_search_field AS s join sys_field as f on s.tableid=f.tableid and s.fieldid=f.fieldid  WHERE s.tableid='{tableid}'"
        )
        result = dictfetchall(cursor)
        if result:
            search_fields = result
    for search_field_key, search_field in enumerate(search_fields):
        context_search_field = dict()
        context_search_field['search_field'] = search_field
        search_fields[search_field_key]['component'] = render_to_string('components/search_field.html',
                                                                        context_search_field, request)

    context['search_fields'] = search_fields
    return user_agent(request, 'content/records.html', 'content/records_mobile.html', context)
    # return render(request, 'content/records.html', context)


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


def get_records_linked(request):
    tableid = request.POST.get('tableid')
    master_tableid = request.POST.get('master_tableid')
    master_recordid = request.POST.get('master_recordid')
    records_table = get_records_table(request, tableid, master_tableid, master_recordid)
    return HttpResponse(records_table)


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


@login_required(login_url='/login/')
def get_test(request):
    num = 1
    return render(request, 'content/test.html', {'num': num})


@login_required(login_url='/login/')
def get_block_reload(request):
    return render(request)


@login_required(login_url='/login/')
def get_render_content_dashboard(request):
    context = {}
    context['blocks'] = []  # Initialize the blocks list
    user_id = request.user.id

    with connection.cursor() as cursor2:
        cursor2.execute(
            "SELECT dashboardid FROM v_user_dashboard_block WHERE bixid = %s", [user_id]
        )
        rows = cursor2.fetchall()
        for row in rows:
            dashboard_id = row[0]

    if request.method == 'POST':
        selected = ''
        with connection.cursor() as cursor:
            cursor.execute(
                "SELECT * FROM v_sys_dashboard_block WHERE dashboardid = %s", [dashboard_id]
            )
            rows = dictfetchall(cursor)

            for row in rows:
                selected = ''
                if row['operation'] == 'somma':
                    fields = row['fieldid'].split(';')
                    for field in fields:
                        field = 'ROUND(SUM(' + field + '))'
                        selected += field + ','
                    groupby = row['groupby']
                    selected += groupby

                query_conditions = row['query_conditions']
                userid = get_userid(request.user.id)
                query_conditions = query_conditions.replace("$userid$", str(userid))
                id = row['id']
                tableid = row['tableid']
                name = row['name']
                layout = row['layout']
                sql = "SELECT " + selected + " FROM " + tableid + \
                      " WHERE " + query_conditions + " GROUP BY " + groupby
                block = dict()
                block['sql'] = sql
                block['name'] = 'test'
                block['html'] = get_chart(request, sql, id, name, layout, fields)
                context['blocks'].append(block)

    return user_agent(request, 'content/dashboard.html', 'content/dashboard_mobile.html', context)


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

    return render_to_string('other/barchart.html', context, request=request)


@login_required(login_url='/login/')
def record_card_duplicate(request):
    return render(request)


@login_required(login_url='/login/')
def record_card_copy(request):
    link = request.POST.get('link')
    pyperclip.copy(link)

    return True


@login_required(login_url='/login/')
def get_record_card_delete(request):
    if request.method == 'POST':
        recordid = request.POST.get('recordid')
        tableid = request.POST.get('tableid')

        with connection.cursor() as cursor:
            query = 'UPDATE user_' + tableid + ' SET deleted_ = "Y" WHERE id = ' + recordid
            cursor.execute(
                query
            )
    return JsonResponse({'success': True})


# https://openclassrooms.com/en/courses/7107341-intermediate-django/7263317-create-a-login-page-with-a-function-based-view


def get_render_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')

            else:
                messages.error(request, 'Invalid username or password')

            """if username == 'admin' and password == 'admin':

                return redirect('index')
            else:
                form.add_error(None, "Invalid username or password")"""

    else:
        form = LoginForm()
    # return user_agent(request, 'other/login.html', 'other/test_query.html', {'form': form})
    return render(request, 'other/../templates/registration/login.html', {'form': form}, )


@user_passes_test(lambda u: u.is_superuser)
def get_render_gestione_utenti(request):
    return render(request, 'other/gestione_utenti.html')


#   @login_required(login_url='/login/')
def get_render_logout(request):
    logout(request)
    return redirect('login')


@login_required(login_url='/login/')
def get_records_table_render(request):
    tableid = request.POST.get('tableid')
    master_tableid = request.POST.get('master_tableid')
    master_recordid = request.POST.get('master_recordid')
    searchTerm = request.POST.get('searchTerm')
    viewid = request.POST.get('viewid')
    currentpage = request.POST.get('currentpage')
    if (currentpage == ''):
        currentpage = 1
    render = get_records_table(request, tableid, master_tableid, master_recordid, searchTerm, viewid, currentpage)
    return HttpResponse(render)


@login_required(login_url='/login/')
def get_records_table(request, tableid, master_tableid='', master_recordid='', searchTerm='', viewid='', currentpage=1):
    userid = get_userid(request.user.id)
    table_type = 'standard'
    table_height = '100%'
    if master_tableid:
        table_height = '500px'
        table_type = 'linked'

    post = {
        'tableid': tableid,
        'searchTerm': searchTerm,
        'viewid': viewid,
        'currentpage': currentpage,
        'master_tableid': master_tableid,
        'master_recordid': master_recordid,
        'userid': userid
    }
    response = requests.post(
        f"{bixdata_server}bixdata/index.php/rest_controller/get_records", data=post)
    response_dict = json.loads(response.text)
    columns = response_dict['columns']
    records = response_dict['records']
    reports = response_dict['reports']
    other_values = dict()
    context = {
        'records': records,
        'reports': reports,
        'columns': columns,
        'tableid': tableid,
        'table_height': table_height,
        'table_type': table_type,
        'other_values': other_values,
        'currentpage': currentpage
    }

    for records_index, record in enumerate(records):
        for record_index, value in enumerate(record):
            record[record_index] = dict()
            record[record_index]['value'] = value
            record[record_index]['code'] = value
            record[record_index]['fieldtype'] = columns[record_index]['fieldtypeid'];
            record[record_index]['fieldtypeweb'] = columns[record_index]['fieldtypewebid'];
            if record[record_index]['fieldtype'] == 'linked':
                if isinstance(value, str):
                    value = value.split('|:|')
                    if (len(value) > 2):
                        record[record_index]['value'] = value[0]
                        record[record_index]['link_recordid'] = value[1]
                        record[record_index]['link_tableid'] = value[2]
                        record[record_index]['fieldtype'] = 'linked'
            if record[record_index]['fieldtype'] == 'Utente':
                code = record[record_index]['code']
                code = code.replace(' ', '.')
                code = code.lower()
                record[record_index]['code'] = code
            if record[record_index]['fieldtype'] == 'Numero':
                string_num = record[record_index]['value']
                if string_num:
                    try:
                        num = float(string_num)
                    except ValueError:
                        num = 0
                else:
                    num = 0
                record[record_index]['value'] = format(num, ".2f")
            if record[record_index]['value'] == 'Validazionetecnica':
                record[record_index]['fieldtype'] = 'lookup'
                record[record_index]['fieldbackground'] = 'green'
            if record[record_index]['value'] == 'Controllosolvibilita':
                record[record_index]['fieldtype'] = 'lookup'
                record[record_index]['fieldbackground'] = 'red'
            if record[record_index]['value'] == 'Chiusovinto':
                record[record_index]['fieldtype'] = 'lookup'
                record[record_index]['fieldbackground'] = 'blue'

        records[records_index] = record

    records_table = bix_render_to_string('block/records/records_table.html', context, request)
    return records_table


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
    tableid = request.POST.get('tableid')
    searchTerm = request.POST.get('searchTerm')
    viewid = request.POST.get('viewid')
    post = {
        'tableid': tableid,
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
        'tableid': tableid,
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
        'block/records/records_calendar.html', context, request=request)
    return HttpResponse(records_table)


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


@login_required(login_url='/login/')
def request_block_record_card(request):
    tableid = request.POST.get('tableid')
    recordid = request.POST.get('recordid')
    userid = request.user.id
    return HttpResponse(get_block_record_card(tableid, recordid, userid))


def get_block_record_card(tableid, recordid, userid):
    context = dict()
    context['block_record_badge'] = get_block_record_badge(tableid, recordid)
    context['block_record_linked'] = get_block_record_linked(tableid, recordid)
    context['block_record_fields'] = ""
    context['recordid'] = recordid
    context['tableid'] = tableid
    context['user_table_settings'] = get_user_table_settings(userid, tableid)
    # returned = user_agent(request, 'block/record/record_card.html', 'block/record/record_card_mobile.html', context)
    return render_to_string('block/record/record_card.html', context)


@login_required(login_url='/login/')
def request_block_record_badge(request, http_response=False):
    tableid = request.POST.get('tableid')
    recordid = request.POST.get('recordid')
    return get_block_record_badge(tableid, recordid)


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


@login_required(login_url='/login/')
def get_block_record_fields(request):
    context = dict()
    http_response = request.POST.get('http_response')
    tableid = request.POST.get('tableid')
    recordid = request.POST.get('recordid')
    master_tableid = request.POST.get('master_tableid')
    master_recordid = request.POST.get('master_recordid')
    contextfunction = request.POST.get('contextfunction')
    with connection.cursor() as cursor:
        cursor.execute("SELECT id FROM sys_user WHERE bixid = %s", [request.user.id])
        row = cursor.fetchone()
        if row:
            userid = row[0]
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
    context['record_fields_labels'] = response_dict
    context['contextfunction'] = contextfunction
    context['tableid'] = tableid
    context['recordid'] = recordid
    context['master_tableid'] = master_tableid
    context['master_recordid'] = master_recordid
    block_record_fields = render_to_string(
        'block/record/record_fields.html', context, request=request)
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
    tableid = ''
    recordid = ''
    fields = ''

    tableid = request.POST.get('tableid')
    recordid = request.POST.get('recordid')
    fields = request.POST.get('fields')

    post_data = {
        'tableid': tableid,
        'recordid': recordid,
        'fields': fields
    }

    response = requests.post(
        f"{bixdata_server}bixdata/index.php/rest_controller/set_record", data=post_data)

    fields_dict = json.loads(fields)

    if tableid == 'ticketbixdata' and 'description' in fields_dict:
        message = 'Nuovo ticket aperto da {} \nDescrizione: {}\nTipo: {}'.format(
            request.user.username, fields_dict['description'], fields_dict.get('type', 'N/A'))
        send_email(request, ['marco.garganigo@swissbix.ch', 'alessandro.galli@swissbix.ch'], 'Supporto bixdata',
                   message)

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

    with connection.cursor() as cursor:
        cursor.execute("SELECT id FROM sys_user WHERE bixid = %s", [request.user.id])
        row = cursor.fetchone()
        if row:
            id = row[0]

    if request.method == 'POST':
        layout = request.POST.get('record_open_layout')
        theme = request.POST.get('theme')

        with connection.cursor() as cursor:
            cursor.execute(
                "UPDATE v_sys_user_settings SET value = %s WHERE userid = %s AND setting = 'record_open_layout'",
                [layout, id]
            )
            cursor.execute(
                "UPDATE v_sys_user_settings SET value = %s WHERE userid = %s AND setting = 'theme'",
                [theme, id]
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
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM sys_user_dashboard"
                       )
        rows = dictfetchall(cursor)

        userids = [row['userid'] for row in rows]
        dashboardids = [row['dashboardid'] for row in rows]

    with connection.cursor() as cursor2:
        cursor2.execute(
            "SELECT firstname, lastname FROM sys_user where id in (SELECT userid FROM sys_user_dashboard)"
        )
        rows2 = dictfetchall(cursor2)

        names = [row['firstname'] + ' ' + row['lastname'] for row in rows2]

    with connection.cursor() as cursor3:
        cursor3.execute(
            "SELECT * FROM v_sys_dashboard_block"
        )
        rows3 = dictfetchall(cursor3)

        chart_names = [row['name'] for row in rows3]
        chart_dashboard_id = [row['dashboardid'] for row in rows3]

    with connection.cursor() as cursor4:
        cursor4.execute(
            "SELECT * FROM sys_view"
        )
        rows4 = dictfetchall(cursor4)

    with connection.cursor() as cursor5:
        cursor5.execute(
            "SELECT * FROM sys_report"
        )
        rows5 = dictfetchall(cursor5)

    context = {
        'userids': userids,
        'dashboardids': dashboardids,
        'names': names,
        'chart_names': chart_names,
        'chart_dashboard_id': chart_dashboard_id,
        'views': rows4,
        'reports': rows5,

    }

    return render(request, f'admin_settings/{page}.html', {'context': context})


@login_required(login_url='/login/')
def save_chart_settings(request):
    if request.method == 'POST':
        userids = request.POST.getlist('userids[]')
        dashboardids = request.POST.getlist('dashboardids[]')
        names = request.POST.getlist('chartnames[]')
        chartdashboardids = request.POST.getlist('chartdashboardids[]')

        with connection.cursor() as cursor:
            for i in range(len(userids)):
                user_id = userids[i]
                dashboard_id = dashboardids[i]

                cursor.execute('UPDATE sys_user_dashboard SET dashboardid = %s WHERE userid = %s',
                               [dashboard_id, user_id])

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

        with connection.cursor() as cursor:
            cursor.execute(
                'INSERT INTO sys_dashboard_block (dashboardid, name, userid, viewid, reportid) VALUES (%s, %s, %s, %s, %s)',
                [dashboard_id, name, 1, view_id, report_id])
    return redirect('index')


@login_required(login_url='/login/')
def get_record_path(request, tableid, recordid):
    userid = request.user.id
    content = get_block_timesheetinvoice(recordid, userid)
    return get_render_index(request, content)


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


def stampa_rapportino(request):
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
        content = render_to_string('content/test.html', row)
        pdfkit.from_string(content, filename, configuration=config)

        # Open the file and read its contents
        with open(filename, 'rb') as file:
            file_data = file.read()

        # Delete the file from the file system
        os.remove(filename)

        # Create an HTTP response with the file contents
        response = HttpResponse(file_data, content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="{filename}"'
        return response




