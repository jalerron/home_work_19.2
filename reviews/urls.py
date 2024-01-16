from django.urls import path

from reviews.apps import ReviewsConfig
from reviews.views import ReviewsCreateView, ReviewsListView, ReviewDetailView, ReviewUpdateView, ReviewDeleteView

app_name = ReviewsConfig.name

urlpatterns = [
    path('create/', ReviewsCreateView.as_view(), name='create'),
    path('reviews/<int:product_id>', ReviewsListView.as_view(), name='list_reviews'),
    path('review/<int:pk>', ReviewDetailView.as_view(), name='view_review'),
    path('edit/<int:pk>', ReviewUpdateView.as_view(), name='edit_review'),
    path('delete/<int:pk>', ReviewDeleteView.as_view(), name='delete_review'),
]
