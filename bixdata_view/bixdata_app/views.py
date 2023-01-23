from django.shortcuts import render
from django.http import HttpResponse
import requests
import json
import datetime


def get_render_index(request):
    response = requests.get(
        "http://10.0.0.133:8822/bixdata/index.php/rest_controller/get_tables_menu")
    menu_list = json.loads(response.text)

    print(menu_list.items())
    print(type(menu_list))
    for workspace_key, workspace_value in menu_list.items():
        print(type(workspace_value))
        for table in workspace_value:
            print(type(table))
            print(table.get('description'))

    context = {
        'menu_list': menu_list,
        'date': datetime.datetime.now().strftime('%Y-%m-%d-%H:%M:%S'),

    }

    return render(request, 'index.html', context)


def get_render_loading(request):
    return render(request, 'other/loading.html')

#request: {tableid}
def get_render_content_records_view(request):
    return render(request, 'content/records_view.html')
