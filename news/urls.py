from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'news'

urlpatterns = [
    path('', views.NewsListView.as_view(), name='list'),
    path('noticias/crear/', views.NewsCreateView.as_view(), name='create'),
    path('noticias/editar/<int:pk>/', views.NewsUpdateView.as_view(), name='edit'),
    path('noticias/<int:pk>/', views.NewsDetailView.as_view(), name='detail'),
    path('noticias/eliminar/<int:pk>/', views.NewsDeleteView.as_view(), name='delete'),
    path('cargar_noticias/', views.load_news, name='load_news'),
    #Category
    path('tematicas', views.CategoryListView.as_view(), name='category_list'),
    path('tematicas/crear/', views.CategoryCreateView.as_view(), name='category_create'),
    path('tematicas/editar/<int:pk>/', views.CategoryUpdateView.as_view(), name='category_edit'),
    path('tematicas/<int:pk>/', views.CategoryDetailView.as_view(), name='category_detail'),
    path('tematicas/eliminar/<int:pk>/', views.CategoryDeleteView.as_view(), name='category_delete'),
]

