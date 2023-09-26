from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.http import HttpResponse

class HelperView:
    
    def __init__(self,request):
        self.request=request
        self.context=dict()
    
    def render_template(self,template_path):
        string_template = self.get_template(template_path)
        return HttpResponse(string_template)
    
    def get_template(self,template_path):
        return render_to_string(template_path, self.context)