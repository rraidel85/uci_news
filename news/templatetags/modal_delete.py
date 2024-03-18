from django import template

register = template.Library()


@register.inclusion_tag('ui/modal/modal_delete.html')
def modal_delete(modal_title=None, modal_description=None):
    """
    Crea una etiqueta para generar un modal para eliminar un elemento.
    """
    return {
        'modal_title': modal_title,
        'modal_description': modal_description,
    }
