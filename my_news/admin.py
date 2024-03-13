from django.contrib import admin

from .models import CategoryModel, ProductModel


# Register your models here.


@admin.register(CategoryModel)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['category_title', 'created_at']
    search_fields = ['category_title']
    list_filter = ['created_at']
    ordering = ['category_title']


@admin.register(ProductModel)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['news_title', 'news_description', 'news_image', 'news_created_at']
    search_fields = ['news_title']
    list_filter = ['news_created_at']