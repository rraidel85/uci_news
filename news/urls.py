from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'news'

urlpatterns = [
    path('', views.NewsListView.as_view(), name='list'),
    path('create/', views.NewsCreateView.as_view(), name='create'),
    path('edit/<int:pk>/', views.NewsUpdateView.as_view(), name='edit'),
    path('news/<int:pk>/', views.NewsDetailView.as_view(), name='detail'),
    path('delete/<int:pk>/', views.NewsDeleteView.as_view(), name='delete'),
]

