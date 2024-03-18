from django import template

register = template.Library()


@register.inclusion_tag('form_generic/form_generic.html')
def form_generic(form, column_size=6):
    """
    Crea una etiqueta para generar un formulario.
    """
    return {
        'form': form,
        'column_size': column_size
    }
