from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.http import Http404
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from catalog.forms import ProductForm, VersionForm, ModeratorProductForm, SuperModeratorProductForm, AdminProductForm
from catalog.models import Product, Version, Category
from catalog.services import get_category_cache
from config import settings
from users.models import User


class ProductListView(LoginRequiredMixin, ListView):
    model = Product
    context_object_name = 'object_list'

    def get_queryset(self, **kwargs):
        queryset = super().get_queryset()
        queryset = Product.objects.filter(is_active=True)
        return queryset

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


class ProductMederationListView(LoginRequiredMixin, ListView):
    model = Product
    context_object_name = 'object_list'

    def get_queryset(self, **kwargs):
        queryset = super().get_queryset()
        queryset = Product.objects.filter(is_active=False)
        return queryset


class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product


class ProductCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:product_list')
    permission_required = 'catalog.add_product'

    def form_valid(self, form):
        new_product = form.save()
        form.save()
        new_product.user = self.request.user
        new_product.user.user_permissions.add(45, 46, 47)
        new_product.save()
        return super().form_valid(form)

    def get_object(self, *args, **kwargs):
        product = super().get_object(*args, **kwargs)
        if product.user == self.request.user or self.request.user.is_superuser or self.request.user.is_staff:
            return product
        return reverse('catalog:product_list')


class ProductUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Product
    # fields = ('name', 'description', 'image', 'category', 'price_for_one', 'is_active')

    success_url = reverse_lazy('catalog:product_list')

    permission_required = [
        'catalog.change_category_product',
        'catalog.change_description_product',
        'catalog.set_active'
    ]

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.object.user != self.request.user and not self.request.user.is_staff:
            raise Http404("Вы не являетесь владельцем этого товара")
        return self.object

    def get_form_class(self):
        if self.request.user.is_superuser:
            return AdminProductForm
        elif (self.request.user == self.get_object().user) and self.request.user.is_staff:
            return SuperModeratorProductForm
        elif (self.request.user == self.get_object().user) and not self.request.user.is_staff:
            return ProductForm
        else:
            return ModeratorProductForm


class ProductDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:product_list')
    permission_required = 'catalog.delete_product'


class VersionCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Version
    form_class = VersionForm
    success_url = reverse_lazy('catalog:product_list')
    permission_required = 'catalog.add_version'

@login_required
def index(request):
    product_list = Product.objects.filter(is_new=True, is_active=True)[:3]
    content = {
        'object_list': product_list,
        'title_head': 'Skystore',
        'title': 'Skystore'
    }
    return render(request, 'catalog/index.html', content)


@login_required
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


class ModeratorProductsView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Product
    permission_required = [
        'catalog.change_category_product',
        'catalog.change_description_product',
        'catalog.set_active'
    ]

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.is_staff or self.request.user.is_superuser:
            return queryset.all()

        products = Product.objects.filter(user=self.request.user)
        queryset = products
        return queryset


class CategoryListView(LoginRequiredMixin, ListView):
    model = Category

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)
        if settings.CACHE_ENABLED:
            context_data['category_list'] = get_category_cache()
            # print(context_data)
        else:
            context_data['category_list'] = Category.objects.all()
        return context_data
