from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.http import HttpResponse

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
    
