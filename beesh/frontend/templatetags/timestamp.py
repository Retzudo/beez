from datetime import datetime

from django import template

register = template.Library()


@register.filter
def date_from_timestamp(timestamp):
    return datetime.fromtimestamp(timestamp)
