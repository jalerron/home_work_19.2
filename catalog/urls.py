from django.urls import path

from catalog.views import (
    index, contacts, ProductListView,
    ProductDetailView, ProductCreateView,
    ProductDeleteView, ProductUpdateView,
    VersionCreateView, ProductMederationListView
)
from catalog.apps import CatalogConfig
from reviews.views import ReviewsListView

app_name = CatalogConfig.name

urlpatterns = [
    path('', index, name='index'),
    path('moderation/', ProductMederationListView.as_view(), name='moderation_list'),
    path('catalog/', ProductListView.as_view(), name='product_list'),
    path('contacts/', contacts, name='contacts'),
    path('product_detail/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('reviews/<int:product_id>/', ReviewsListView.as_view(), name='list_reviews'),
    path('create_product/', ProductCreateView.as_view(), name='create_product'),
    path('update/<int:pk>', ProductUpdateView.as_view(), name='update_product'),
    path('delete/<int:pk>', ProductDeleteView.as_view(), name='delete_product'),
    path('add_version/', VersionCreateView.as_view(), name='create_version')

]

