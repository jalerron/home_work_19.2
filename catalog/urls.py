from django.urls import path

from catalog.views import index, contacts, ProductListView, ProductDetailView
from catalog.apps import CatalogConfig
from reviews.views import ReviewsListView

app_name = CatalogConfig.name

urlpatterns = [
    path('', index, name='index'),
    path('catalog/', ProductListView.as_view(), name='product_list'),
    path('contacts/', contacts, name='contacts'),
    path('product_detail/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('reviews/<int:product_id>/', ReviewsListView.as_view(), name='list_reviews')
]
