import json
import time
from django.db import connection, connections
from django.http import HttpResponse
from django.shortcuts import render
from bixdata_app.models import *
from .alpha import staff_only
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.interval import IntervalTrigger
from apscheduler.jobstores.memory import MemoryJobStore
from apscheduler.executors.pool import ThreadPoolExecutor

@staff_only
def scheduler(request):
    tasks = SysSchedulerTasks.objects.all().values()

    running_tasks = SysSchedulerTasks.objects.filter(status='running').values()

    if running_tasks:
        button = 'stop'
    else:
        button = 'run'

    data = {
        'tasks': tasks,
        'button': button
    }

    return render(request, 'scheduler/scheduler.html', data)


def schedule_job(request, funzione, interval):
    global scheduler
    scheduler = BackgroundScheduler()
    if funzione in globals() and callable(globals()[funzione]):
        func = globals()[funzione]
        scheduler.add_job(func, 'interval', seconds=interval)
    scheduler.start()

def funzionetest2():
    with connection.cursor() as cursor:
        cursor.execute(
            "INSERT INTO sys_scheduler_log (funzione,output) VALUES ('funzionetest2','funzionetest2 log')"
        )
    print('funzionetest2')


def test_scheduler(request):
    current_time = time.time()
    locks_to_delete = []

    for lock_key, lock_info in locker.locks.items():
        lock_timestamp = lock_info['timestamp']
        lock_user = lock_info['user']
        if lock_user == request.user.id:
            if current_time - lock_timestamp > 10:
                locks_to_delete.append(lock_key)

    with locker.lock:  # Use the lock for thread safety
        for lock_key in locks_to_delete:
            del locker.locks[lock_key]

    if lock.locked():
        return False



def save_scheduler_settings(request):
    tasks = request.POST.getlist('tasks')
    tasks = json.loads(tasks[0])

    with connection.cursor() as cursor:
        for task in tasks:
            name = task['name']
            value = task['value']

            SysSchedulerTasks.objects.filter(funzione=name).update(active=value)

            if value == '0':
                SysSchedulerTasks.objects.filter(funzione=name).update(active=value, status='stopped')

    return HttpResponse('Settings saved successfully')


def run_tasks(request):
    button = request.POST.get('button')

    if button == 'run':

        tasks = SysSchedulerTasks.objects.filter(active=1).values()

        if tasks:
            with connection.cursor() as cursor:
                for task in tasks:
                    funzione = task['funzione']

                    SysSchedulerTasks.objects.filter(funzione=funzione).update(status='running')

                    schedule_job(request, funzione, task['intervallo'])
                    button = 'stop'

    else:
        stop_job()

        tasks = SysSchedulerTasks.objects.filter(active=1).values()

        if tasks:
            for task in tasks:
                funzione = task['funzione']

                SysSchedulerTasks.objects.filter(funzione=funzione).update(status='stopped')
                button = 'run'

    return button


def stop_job():
    global scheduler

    if scheduler is not None:
        scheduler.shutdown()
        scheduler.remove_all_jobs()
        scheduler = None