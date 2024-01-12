from django import forms
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.text import slugify
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from catalog.forms import ProductForm
from catalog.models import Product, Version


class ProductListView(ListView):
    model = Product
    context_object_name = 'object_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        for product in context['object_list']:
            active_version = product.version_set.filter(is_active=True).first()

            if active_version:
                product.active_version_number = active_version.num_version
                product.active_version_name = active_version.name
            else:
                product.active_version_number = None
                product.active_version_name = None

        return context


class ProductDetailView(DetailView):
    model = Product


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:product_list')


class ProductUpdateView(UpdateView):
    model = Product
    fields = ('__all__')
    success_url = reverse_lazy('catalog:product_list')


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:product_list')


class VersionCreateView(CreateView):
    model = Version
    success_url = reverse_lazy('catalog:product_list')


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
