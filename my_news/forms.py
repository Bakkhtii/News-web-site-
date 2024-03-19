
from django import forms

from .models import ProductModel


class CreateProductForm(forms.ModelForm):
    news_title = forms.CharField()
    news_description = forms.CharField()
    news_image = forms.FileField()

    class Meta:
        model = ProductModel
        fields = ['news_title', 'news_description', 'news_image',]


class UpdateProductForm (forms.ModelForm):
    news_title = forms.CharField()
    news_description = forms.CharField()
    news_image = forms.FileField()

    class Meta:
        model = ProductModel
        fields = ['news_title', 'news_description', 'news_image',]
