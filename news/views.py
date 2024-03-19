from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .models import News

class NewsListView(ListView):
    model = News
    template_name = 'news/news_list.html'

class NewsCreateView(CreateView):
    model = News
    fields = '__all__'
    template_name = 'news/news_form.html'

class NewsUpdateView(UpdateView):
    model = News
    fields = '__all__'
    template_name = 'news/news_form.html'
    
class NewsDetailView(DetailView):
    model = News
    template_name = 'news/news_detail.html'

class NewsDeleteView(DeleteView):
    model = News
    template_name = 'news/news_confirm_delete.html'
    success_url = '/news/'