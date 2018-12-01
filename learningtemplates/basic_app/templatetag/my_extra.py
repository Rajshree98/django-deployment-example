from django import template

register=template_Library()

@register.filter(name='cut')

def cut(value,arg):
          return replace(arg,"")
