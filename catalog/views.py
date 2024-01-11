from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.text import slugify
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from catalog.models import Product


class ProductListView(ListView):
    model = Product


class ProductDetailView(DetailView):
    model = Product


class ProductCreateView(CreateView):
    model = Product
    fields = ('__all__')
    success_url = reverse_lazy('catalog:product_list')


class ProductUpdateView(UpdateView):
    model = Product


class ProductDeleteView(DeleteView):
    model = Product


def index(request):
    product_list = Product.objects.filter(is_new=True)[:3]
    content = {
        'object_list': product_list,
        'title_head': 'Skystore',
        'title': 'Skystore'
    }
    return render(request, 'catalog/index.html', content)


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'{name} ({phone}): {message}')

    content = {
        'title_head': 'Skystore',
        'title': 'Контакты',
    }

    return render(request, 'catalog/contacts.html', content)
