from django.contrib import admin
from .models import Category, News

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'pub_date', 'source', 'gender', 'ideological_stance', 'descriptor')
    list_filter = ('category', 'pub_date')
    search_fields = ('title', 'source', 'gender', 'ideological_stance', 'descriptor')
    date_hierarchy = 'pub_date'