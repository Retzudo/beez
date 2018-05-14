from django import template

from core.utils import color_for_year

register = template.Library()


@register.filter
def year_color(year):
    return color_for_year(int(year))