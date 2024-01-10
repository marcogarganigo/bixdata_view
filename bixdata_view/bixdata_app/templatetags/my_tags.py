from django import template 
register = template.Library()
@register.filter(name="get")
def get(indexable, i):
    return indexable[i]