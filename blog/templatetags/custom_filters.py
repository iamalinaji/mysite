from django import template
from datetime import datetime

register = template.Library()

@register.filter
def format_date(value):
    return value.strftime("%B %d, %Y")