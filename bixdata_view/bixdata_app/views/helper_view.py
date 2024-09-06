from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.http import HttpResponse
from bixdata_app.models import *
from .businesslogic.models.database_helper import *
from datetime import datetime
from dateutil.relativedelta import relativedelta

# Questa funzione blocca l'accesso a bixdata da firefox
def firefox_check(view_func):
    def wrapped_view(request, *args, **kwargs):
        user_agent = request.META.get('HTTP_USER_AGENT', '')

        if 'firefox' in user_agent.lower():

            return render(request, 'other/firefox.html')
        else:
            return view_func(request, *args, **kwargs)

    return wrapped_view

class HelperView:
    """Metodi generali di supporto per le altre View
    """
    def __init__(self,request):
        self.request=request
        self.context=dict()
        self.db_helper=DatabaseHelper()
    
    
    def render_template(self,template_path):
        """Generazione del template come pagina html

        Args:
            template_path (str): path del template da usare

        Returns:
            _type_: template generato come pagina html
        """
        string_template = self.get_template(template_path)
        return HttpResponse(string_template)
    
    def get_template(self,template_path):
        """Generazione del template come stringa

        Args:
            template_path (str): path del template da usare

        Returns:
            _type_: template generato come stringa
        """
        return render_to_string(template_path, self.context)
    
    def get_userid(self,request):
        rows = SysUser.objects.filter(bixid=request.user.id).values('id')
        if rows:
            row = row[0]
            userid = row['id']
            return userid
        else:
            return None
        
    def get_userid(self):
        django_userid=self.request.user.id
        userid = 0
        sql=f"SELECT id FROM sys_user WHERE bixid = {django_userid}"
        user=self.db_helper.sql_query_row(sql)
        if(user):
            userid=user['id']
        else:
            userid=None    
        return userid 
    

    from datetime import datetime

    def get_last_occurrence(input_date):
        # Get the current date
        current_date = datetime.now()

        # Parse the input date
        input_date = datetime.strptime(input_date, '%Y-%m-%d')
        input_month = input_date.month
        input_day = input_date.day

        # Initialize the year to the current year
        year = current_date.year

        # Loop backwards year by year until we find the last occurrence
        while True:
            candidate_date = datetime(year, input_month, input_day)

            # Check if this date is before the current date
            if candidate_date <= current_date:
                return candidate_date.strftime('%Y-%m-%d')

            # Decrement the year
            year -= 1


    def get_occurrences_count(input_date):
        # Get the current date
        current_date = datetime.now()

        # Parse the input date
        input_date = datetime.strptime(input_date, '%Y-%m-%d')
        input_month = input_date.month
        input_day = input_date.day

        # Initialize the year to the year of the input date
        start_year = input_date.year
        end_year = current_date.year

        # Initialize the occurrence count
        occurrence_count = 0

        # Loop through the years and count occurrences
        for year in range(start_year, end_year + 1):
            candidate_date = datetime(year, input_month, input_day)

            # Check if this date is before or equal to the current date
            if candidate_date <= current_date:
                occurrence_count += 1

        return occurrence_count
    
    def get_repetition_count(data_inizio, intervallo_mesi):
        # Converti la data di inizio da stringa a oggetto datetime
        data_inizio = datetime.strptime(data_inizio, '%Y-%m-%d')
        
        # Ottieni la data di oggi
        oggi = datetime.today()
        
        # Calcola la differenza in mesi tra oggi e la data di inizio
        delta_anni = oggi.year - data_inizio.year
        delta_mesi = oggi.month - data_inizio.month
        delta_totale_mesi = delta_anni * 12 + delta_mesi
        
        # Calcola quante volte si è ripetuto l'evento
        ripetizioni = delta_totale_mesi // intervallo_mesi + 1
        
        return ripetizioni

    def create_new_userid(self):
        # Get the last user id
        sql = "SELECT MAX(id) AS max_id FROM sys_user"
        max_id = self.db_helper.sql_query_row(sql)
        if max_id:
            new_id = max_id['max_id'] + 1
        else:
            new_id = 1

        return new_id

    
    
    
    
