from django.contrib import messages
from django.contrib.auth import views
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views import View


class UserLoginView(LoginView):
    def form_valid(self, form):
        messages.success(self.request, 'Bienvenid(o) al sistema')
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('news:list')

class PasswordChangeDoneView(LoginRequiredMixin, views.PasswordChangeDoneView):

    def get(self, request, *args, **kwargs):
        messages.success(self.request, 'Su contraseña se ha cambiado correctamente')
        return HttpResponseRedirect(reverse('usuarios:perfil'))


class ProfileDetailView(LoginRequiredMixin, View):

    def get(self, request):
        return render(request, template_name='usuarios/profile/profile_detalles.html')


class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('news:list')

