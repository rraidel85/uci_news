from .models import News
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib import messages
from django.urls import reverse_lazy, reverse
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect

class NewsListView(ListView):
    model = News
    template_name = 'news/news_list.html'
    # permission_required = 'news.view_news'
    context_object_name = 'news'
    
class NewsDetailView(PermissionRequiredMixin, DetailView):
    model = News
    template_name = 'news/news_detail.html'
    permission_required = 'news.view_news'
    context_object_name = 'news'

class NewsCreateView(PermissionRequiredMixin, CreateView):
    model = News
    fields = '__all__'
    template_name = 'news/news_form.html'
    permission_required = 'news.add_news'

    def form_valid(self, form):
        messages.success(self.request, 'Noticia creada correctamente.')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Existen errores en el formulario.')
        return super().form_invalid(form)

    def get_success_url(self):
        return reverse_lazy('news:detail', args=[self.object.id])

class NewsUpdateView(PermissionRequiredMixin, UpdateView):
    model = News
    fields = '__all__'
    template_name = 'news/news_form.html'
    permission_required = 'news.change_news'

    def form_valid(self, form):
        messages.success(self.request, 'Noticia actualizada correctamente.')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Existen errores en el formulario.')
        return super().form_invalid(form)

    def get_success_url(self):
        return reverse_lazy('news:detail', args=[self.object.id])

class NewsDeleteView(PermissionRequiredMixin, DeleteView):
    model = News
    template_name = 'news/news_confirm_delete.html'
    permission_required = 'news.delete_news'

    def get(self, request, pk):
        item = get_object_or_404(News, pk=pk)
        item.delete()
        messages.success(self.request, 'Noticia eliminada correctamente')
        return HttpResponseRedirect(reverse('news:list'))