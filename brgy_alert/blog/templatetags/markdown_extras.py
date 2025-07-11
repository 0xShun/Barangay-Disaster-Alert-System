from django import template
import markdown as md
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter
def markdown(value):
    return mark_safe(md.markdown(value, extensions=['extra', 'codehilite', 'nl2br'])) 