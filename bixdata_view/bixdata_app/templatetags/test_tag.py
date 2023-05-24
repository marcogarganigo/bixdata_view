from django import template

register = template.Library()


@register.simple_tag
def show(val=None):
    if val == 1:
        return 'show'
    else:
        return 'hide'

