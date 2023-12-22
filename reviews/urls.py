from django.urls import path

from reviews.apps import ReviewsConfig

app_name = ReviewsConfig.name

urlpatterns = [
    path('create/', ..., name='create'),
    path('', ..., name='list'),
    path('view/<int:pk>', ..., name='view'),
    path('edit/<int:pk>', ..., name='edit'),
    path('delete/<int:pk>', ..., name='delete'),
]
