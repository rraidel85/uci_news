from django.urls import path, reverse_lazy
from django.contrib.auth import views as auth_views

from usuarios.views import UserLoginView, RegisterView, ProfileUpdateView, ProfileDetailView, PasswordChangeDoneView, CustomLogoutView

app_name = 'usuarios'
urlpatterns = [
    path('login/', UserLoginView.as_view(template_name='usuarios/login.html'), name='login'),
    path('registro/', RegisterView.as_view(), name='register'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),

    path('perfil/', ProfileDetailView.as_view(), name='perfil'),
    path('editar-perfil/', ProfileUpdateView.as_view(), name='editar_perfil'),
    path('cambiar-clave/', auth_views.PasswordChangeView.as_view(template_name='usuarios/profile/change_password.html',
                                                                 success_url=reverse_lazy(
                                                                     'usuarios:password_change_done')), name='cambiar_clave'),
    path('password-change_done/', PasswordChangeDoneView.as_view(),
         name='password_change_done'),
]
