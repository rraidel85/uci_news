from .models import News, Category
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib import messages
from django.urls import reverse_lazy, reverse
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.http import JsonResponse
from django.template.loader import render_to_string

class NewsListView(ListView):
    model = News
    template_name = 'news/news_list.html'
    context_object_name = 'news'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context
    
class NewsListAdminView(PermissionRequiredMixin, ListView):
    model = News
    template_name = 'news/news_admin_list.html'
    permission_required = 'news.view_news'
    context_object_name = 'news'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context
    
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
        return reverse_lazy('news:news_admin')

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
        return reverse_lazy('news:news_admin')

class NewsDeleteView(PermissionRequiredMixin, DeleteView):
    model = News
    template_name = 'news/news_confirm_delete.html'
    permission_required = 'news.delete_news'

    def get(self, request, pk):
        item = get_object_or_404(News, pk=pk)
        item.delete()
        messages.success(self.request, 'Noticia eliminada correctamente')
        return HttpResponseRedirect(reverse('news:news_admin'))
    
    
#Category    
class CategoryListView(PermissionRequiredMixin, ListView):
    model = Category 
    template_name = 'category/category_list.html'
    permission_required = 'news.view_category'
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
        return reverse_lazy('news:category_list')

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
        return reverse_lazy('news:category_list')

class CategoryDeleteView(PermissionRequiredMixin, DeleteView):
    model = Category
    template_name = 'category/category_confirm_delete.html'
    permission_required = 'news.delete_category'

    def get(self, request, pk):
        item = get_object_or_404(Category, pk=pk)
        item.delete()
        messages.success(self.request, 'Temática eliminada correctamente')
        return HttpResponseRedirect(reverse('news:category_list'))
    
    
def load_news(request):
    category = request.GET.get('category', None)
    order = request.GET.get('order', 'desc')
    
    if category != 'any':
        news_items = News.objects.filter(category_id=category).order_by('-pub_date' if order == 'desc' else 'pub_date')
    else:
        news_items = News.objects.all().order_by('-pub_date' if order == 'desc' else 'pub_date')

    # context = {'news': news_items}
    # html = render(request, 'news/news_list_items.html', context).content.decode('utf-8')

    print(news_items)
    html = render_to_string(
            template_name="news/news_list_items.html", 
            context={"news": news_items}
        )

    data_dict = {"html_from_view": html}

    return JsonResponse(data=data_dict, safe=False)