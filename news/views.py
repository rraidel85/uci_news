from .models import News, Category
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
    template_name = 'news/news_update_form.html'
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
    
    
#Category    
class CategoryListView(ListView):
    model = Category 
    template_name = 'category/category_list.html'
    context_object_name = 'categories'
    
class CategoryDetailView(PermissionRequiredMixin, DetailView):
    model = Category
    template_name = 'category/category_detail.html'
    permission_required = 'news.view_category'
    context_object_name = 'category'

class CategoryCreateView(PermissionRequiredMixin, CreateView):
    model = Category
    fields = '__all__'
    template_name = 'category/category_form.html'
    permission_required = 'news.add_category'

    def form_valid(self, form):
        messages.success(self.request, 'Temática creada correctamente.')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Existen errores en el formulario.')
        return super().form_invalid(form)

    def get_success_url(self):
        return reverse_lazy('news:category_detail', args=[self.object.id])

class CategoryUpdateView(PermissionRequiredMixin, UpdateView):
    model = Category
    fields = '__all__'
    template_name = 'category/category_update_form.html'
    permission_required = 'news.change_category'

    def form_valid(self, form):
        messages.success(self.request, 'Temática actualizada correctamente.')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Existen errores en el formulario.')
        return super().form_invalid(form)

    def get_success_url(self):
        return reverse_lazy('news:category_detail', args=[self.object.id])

class CategoryDeleteView(PermissionRequiredMixin, DeleteView):
    model = Category
    template_name = 'category/category_confirm_delete.html'
    permission_required = 'news.delete_category'

    def get(self, request, pk):
        item = get_object_or_404(Category, pk=pk)
        item.delete()
        messages.success(self.request, 'Temática eliminada correctamente')
        return HttpResponseRedirect(reverse('news:category_list'))