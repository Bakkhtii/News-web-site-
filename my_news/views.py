from django.shortcuts import render
from django.views.generic import CreateView, UpdateView
from django.urls import reverse_lazy
from my_news.models import CategoryModel, ProductModel

from .forms import CreateProductForm, UpdateProductForm


# Create your views here.


def home_page(request):
    categories = CategoryModel.objects.all()
    news = ProductModel.objects.all()
    context = {'categories': categories, 'news': news}
    return render(request, template_name='index.html', context=context)


class ProductCreateView(CreateView):
    model = ProductModel
    template_name = 'create.html'
    form_class = CreateProductForm

    def get_success_url(self):
        return '/'


class ProductUpdateView(UpdateView):
    model = ProductModel
    template_name = 'update.html'
    form_class = UpdateProductForm
    success_url = reverse_lazy('/')
