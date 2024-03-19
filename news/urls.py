"""
URL configuration for news project.

The `urlpatterns` list routes URLs to views. For more information please see:

"""
from django.contrib import admin

from django.urls import path

from my_news.views import home_page, ProductCreateView, ProductUpdateView

from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_page),
    path('create',  ProductCreateView.as_view()),
    path('update/<int:pk>',  ProductUpdateView.as_view()),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
