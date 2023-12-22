from django.urls import path

from reviews.apps import ReviewsConfig
from reviews.views import ReviewsCreateView, ReviewsListView

app_name = ReviewsConfig.name

urlpatterns = [
    path('create/', ReviewsCreateView.as_view(), name='create'),
    path('<int:product_id>/', ReviewsListView.as_view(), name='list'),
    # path('view/<int:pk>', ..., name='view'),
    # path('edit/<int:pk>', ..., name='edit'),
    # path('delete/<int:pk>', ..., name='delete'),
]
