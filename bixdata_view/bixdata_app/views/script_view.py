from .alpha import *
from .helper_view import *
from django.db.models import OuterRef, Subquery
from .businesslogic.settings_business_logic import *
from .businesslogic.script_logic import *


def script_test(request):
    bl=ScriptLogic()
    return HttpResponse('test')
    
def script_call(request,function):
    """Esegue una funzione

    Args:
        request (_type_): richiesta d'origin
        function (str): funzione da eseguire

    Returns:
        str: risultato della funzione chiamata, visualizzabile  nel browser
    """
    if function in globals() and callable(globals()[function]):
        func = globals()[function]
        return func()
    
def update_deals():
    """Aggiorna tutti i dati delle trattative (segnate come da aggiornare) in bixdata, calcolando totali, margini ecc e recuperando informazioni aggiuntive dalla trattativa in Adiuto

    Returns:
        HttpResponse: risultato della funzione
    """
    script_logic=ScriptLogic()
    result=script_logic.update_deals()
    return HttpResponse(result)