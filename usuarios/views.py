from django.contrib import messages
from django.contrib.auth import views, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.models import Group
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import FormView, CreateView
from usuarios.forms import UpdateProfileForm, RegisterForm

class UserLoginView(LoginView):
    def form_valid(self, form):
        messages.success(self.request, 'Bienvenid(o) al sistema')
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('news:list')

class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = "usuarios/register.html"
    success_url = reverse_lazy("news:list")

    def form_valid(self, form):
        user = form.save()
        lector_group = Group.objects.get(name='Lector')
        lector_group.user_set.add(user)
        # Log in the user
        login(self.request, user)
        return super().form_valid(form)

class PasswordChangeDoneView(LoginRequiredMixin, views.PasswordChangeDoneView):

    def get(self, request, *args, **kwargs):
        messages.success(self.request, 'Su contraseña se ha cambiado correctamente')
        return HttpResponseRedirect(reverse('usuarios:perfil'))


class ProfileDetailView(LoginRequiredMixin, View):

    def get(self, request):
        return render(request, template_name='usuarios/profile/profile_detalles.html')


class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('news:list')

class ProfileUpdateView(LoginRequiredMixin, FormView):
    template_name = 'usuarios/profile/profile_update.html'

    def get_form(self):
        return UpdateProfileForm(instance=self.request.user)

    def post(self, request, *args, **kwargs):
        form = UpdateProfileForm(request.POST, instance=self.request.user)

        if form.is_valid():
            form.save()
            messages.success(self.request, 'Perfil actualizado correctamente.')
            return HttpResponseRedirect(reverse('usuarios:perfil'))
        else:
            messages.error(self.request, 'Existen errores en el formulario.')
            return self.get(self, request)

    def get_success_url(self):
        return reverse_lazy('usuarios:perfil')
