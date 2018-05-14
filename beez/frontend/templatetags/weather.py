from django import template

register = template.Library()

icon_map = {
    'Rain': 'day-rain',
    'Snow': 'day-snow',
}


@register.filter
def weather_icon(condition):
    return icon_map.get(condition, 'day-sunny')
