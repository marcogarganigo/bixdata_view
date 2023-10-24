from .alpha import *
from .helper_view import *
from django.db.models import OuterRef, Subquery
from .businesslogic.settings_business_logic import *
from .businesslogic.script_business_logic import *


def script_test(request):
    bl=ScriptBusinessLogic()
    return HttpResponse('test')
    
def script_call(request,function):
    bl=ScriptBusinessLogic()
    result=bl.update_deals()
    
def update_deals():
    bl=ScriptBusinessLogic()
    result=bl.update_deals()