from datetime import datetime
from O365 import Account
import sys
import environ


class OfficeCalendar:

    def __init__(self):
        env = environ.Env()
        self.credentials = (env('CLIENT_ID'), env('SECRET_ID'))
        self.account = Account(self.credentials, auth_flow_type='credentials', tenant_id=env('TENANT_ID'))


    def add_calendar_event(request, task):
        #pick the env variables from the __init__
        env = environ.Env()
        environ.Env.read_env()
        credentials = (env('CLIENT_ID'), env('SECRET_ID'))
        account = Account(credentials, auth_flow_type='credentials', tenant_id=env('TENANT_ID'))



        if account.authenticate():
            print('Authenticated!')

            schedule = account.schedule(resource='alessandrogalli@zechinitest.onmicrosoft.com')
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

                #event.task_recordid = task['recordid']


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

            schedule = account.schedule(resource='alessandrogalli@zechinitest.onmicrosoft.com')
            calendar = schedule.get_default_calendar()

            events = calendar.get_events(include_recurring=False)

            return events


    def edit_calendar_event(request):
        env = environ.Env()
        environ.Env.read_env()

        credentials = (env('CLIENT_ID'), env('SECRET_ID'))

        account = Account(credentials, auth_flow_type='credentials', tenant_id=env('TENANT_ID'))

        if account.authenticate():
            print('Authenticated!')

            schedule = account.schedule(resource='alessandrogalli@zechinitest.onmicrosoft.com')
            calendar = schedule.get_default_calendar()

            q = calendar.new_query('ical_uid').equals(
                '040000008200E00074C5B7101A82E008000000006BF256998306DA010000000000000000100000006C434FF345057849BA1ADC29F02C5531')

            event2_generator = calendar.get_events(query=q, include_recurring=False)

            # Get the first event with the specified ical_uid
            event2 = next(event2_generator, None)




