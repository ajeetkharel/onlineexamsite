from django import template
register = template.Library()

@register.simple_tag
def define(val=None):
  return True