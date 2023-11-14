from datetime import datetime
from O365 import Account
import sys
import environ
from django.db import connection
from django.http import HttpResponse, JsonResponse


class OfficeCalendar:

    def __init__(self):
        env = environ.Env()
        self.credentials = (env('CLIENT_ID'), env('SECRET_ID'))
        self.account = Account(self.credentials, auth_flow_type='credentials', tenant_id=env('TENANT_ID'))

    def add_calendar_event(request, task):
        # pick the env variables from the __init__
        env = environ.Env()
        environ.Env.read_env()
        credentials = (env('CLIENT_ID'), env('SECRET_ID'))
        account = Account(credentials, auth_flow_type='credentials', tenant_id=env('TENANT_ID'))

        if account.authenticate():
            print('Authenticated!')

            schedule = account.schedule(resource=env('EMAIL'))
            calendar = schedule.get_default_calendar()

            if task['o365_idcalendar'] == '':
                # Assuming task['planneddate'] is in the format 'YYYY-MM-DD' and task['start'] and task['end'] are in the format 'HH:MM'
                date_parts = task['planneddate'].split('-')
                year, month, day = map(int, date_parts)

                start_hour, start_minute = map(int, task['start'].split(':'))
                end_hour, end_minute = map(int, task['end'].split(':'))

                event_start = datetime(year, month, day, start_hour, start_minute)
                event_end = datetime(year, month, day, end_hour, end_minute)

                event = calendar.new_event()
                event.subject = "Test evento icaluid"
                event.start = event_start
                event.end = event_end
                event.location = "Test"
                event.body = task['description']

                # event.recordid = task['recordid']

                event.save()

                return event.ical_uid
        else:
            print('Authentication failed!')

    def get_calendar_events(request):

        env = environ.Env()
        environ.Env.read_env()

        credentials = (env('CLIENT_ID'), env('SECRET_ID'))

        account = Account(credentials, auth_flow_type='credentials', tenant_id=env('TENANT_ID'))

        if account.authenticate():
            print('Authenticated!')

            schedule = account.schedule(resource=env('EMAIL'))
            calendar = schedule.get_default_calendar()

            q = calendar.new_query('ical_uid').equals('040000008200E00074C5B7101A82E00800000000848F74993816DA01000000000000000010000000C6404A701B76C844B318927831493923')

            events = calendar.get_events(query=q, include_recurring=False)

            return events

    def update_calendar_event(request, task):
        env = environ.Env()
        environ.Env.read_env()

        credentials = (env('CLIENT_ID'), env('SECRET_ID'))

        account = Account(credentials, auth_flow_type='credentials', tenant_id=env('TENANT_ID'))

        if account.authenticate():
            print('Authenticated!')

            schedule = account.schedule(resource=env('EMAIL'))
            calendar = schedule.get_default_calendar()

            q = calendar.new_query('ical_uid').equals(task['o365_idcalendar'])

            event2_generator = calendar.get_events(query=q, include_recurring=False)

            # Get the first event with the specified ical_uid
            event2 = next(event2_generator, None)

            date_parts = task['planneddate'].split('-')
            year, month, day = map(int, date_parts)

            start_hour, start_minute = map(int, task['start'].split(':'))
            end_hour, end_minute = map(int, task['end'].split(':'))

            event_start = datetime(year, month, day, start_hour, start_minute)
            event_end = datetime(year, month, day, end_hour, end_minute)

            event2.subject = "Test evento icaluid modificato"
            event2.start = event_start
            event2.end = event_end
            event2.location = "Test"
            event2.body = task['description']

            event2.save()

            return HttpResponse({'success': 'true'})
