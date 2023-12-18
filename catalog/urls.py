from django.urls import path

from catalog.views import index, catalog, contacts
from catalog.apps import CatalogConfig

app_name = CatalogConfig.name

urlpatterns = [
    path('', index, name='index'),
    path('catalog/', catalog, name='catalog'),
    path('contacts/', contacts, name='contacts')
]
