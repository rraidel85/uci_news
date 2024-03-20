from django import template
from django.urls import reverse

register = template.Library()


class Menu:
    def __init__(self, title='', icon='', url='', view_url='', submenus=[]):
        self.title = title
        self.icon = icon
        self.url = url
        self.view_url = view_url
        self.submenus = submenus


@register.simple_tag
def custom_menu(user=None):
    """
    Crear un menu personalizable en el template

    return: Devuelve una lista de listas, cada lista contiene un elemento del menu
    """

    menu = [
        Menu('Inicio', 'home', reverse('news:list'), None, []),
        'Divider',
        Menu('Noticias', 'bar-chart-2', reverse('news:news_admin'), None),
        Menu('Temáticas', 'bar-chart-2', reverse('news:category_list'), None),
        'Divider',
        Menu('Administración', 'bar-chart-2', '/admin', None, []),
    ]

    # if 'Administrador' in user.groups.get().name:
    #     menu.extend(
    #         [
    #             'Divider',
    #             ('Category', 'Acceso y seguridad'),  # Category name
    #             Menu('Gestionar usuarios ', 'user', None, None, [
    #                 Menu('Nuevo usuario', '', '', None),
    #                 Menu('Administrar', '', '', None),
    #             ]),
    #         ]
    #     )

    return menu
# @register.simple_tag
# def custom_menu(user=None):
#     """
#     Crear un menu personalizable en el template

#     return: Devuelve una lista de listas, cada lista contiene un elemento del menu
#     """

#     menu = [
#         Menu('Inicio', 'home', reverse('bscmes:index'), None, []),
#         'Divider',
#         ('Category', 'ADMINISTRACIÓN'),  # Category name
#         Menu('Procesos', 'bar-chart-2', None, None, [
#             Menu('Nuevo proceso', '', reverse('bscmes:proceso_crear'), None),
#             Menu('Administrar', '', reverse('bscmes:proceso_administrar'), None),
#         ]),
#         Menu('Unidades orgánicas', 'disc', None, None, [
#             Menu('Nueva unidad orgánica', '', reverse('bscmes:unidad_crear'), None),
#             Menu('Administrar', '', reverse('bscmes:unidad_administrar'), None),
#         ]),
#         Menu('Indicadores', 'list', None, None, [
#             Menu('Nuevo indicador', '', reverse('bscmes:indicador_crear'), None),
#             Menu('Administrar', '', reverse('bscmes:indicador_administrar'), None),
#         ]),

#     ]

#     if 'Administrador' in user.groups.get().name:
#         menu.extend(
#             [
#                 'Divider',
#                 ('Category', 'Acceso y seguridad'),  # Category name
#                 Menu('Gestionar usuarios ', 'user', None, None, [
#                     Menu('Nuevo usuario', '', reverse('usuarios:crear'), None),
#                     Menu('Administrar', '', reverse('usuarios:administrar'), None),
#                 ]),
#             ]
#         )

#     return menu
