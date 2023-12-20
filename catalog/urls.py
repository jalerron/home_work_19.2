from django.urls import path

from catalog.views import index, catalog, contacts, product_detail
from catalog.apps import CatalogConfig

app_name = CatalogConfig.name

urlpatterns = [
    path('', index, name='index'),
    path('catalog/', catalog, name='catalog'),
    path('contacts/', contacts, name='contacts'),
    # path('catalog//', product_detail, name='product_detail')
    path('procuct_detail/<int:product_id>/', product_detail, name='product_detail')
]
