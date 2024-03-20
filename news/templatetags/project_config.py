from django import template
from django.urls import reverse

register = template.Library()


@register.simple_tag
def project_config(name=None, icon=None):
    config = {
        'title': 'Noticias' if not name else name,
        'icon': 'plantilla/assets/images/logo/logo.ico' if not icon else icon,
    }
    return config
