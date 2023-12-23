from django.urls import path

from catalog.views import index, contacts, ProductListView, ProductDetailView
from catalog.apps import CatalogConfig

app_name = CatalogConfig.name

urlpatterns = [
    path('', index, name='index'),
    path('catalog/', ProductListView.as_view(), name='product_list'),
    path('contacts/', contacts, name='contacts'),
    # path('catalog//', product_detail, name='product_detail')
    path('product_detail/<int:pk>/', ProductDetailView.as_view(), name='product_detail')
]
