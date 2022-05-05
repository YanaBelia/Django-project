from django import template
from my_site.models import *

register = template.Library()

@register.simple_tag(name='category')
def func():
    return Category.objects.all()

@register.simple_tag(name='orders')
def func():
    return Orders.objects.all()
