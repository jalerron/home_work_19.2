from django.urls import path

from blogs.apps import BlogsConfig
from blogs.views import BlogsCreateView, BlogsListView, BlogsDetailView, BlogsUpdateView, BlogsDeleteView, \
    BlogsModerationList

app_name = BlogsConfig.name

urlpatterns = [
    path('', BlogsListView.as_view(), name='list'),
    path('moderation/', BlogsModerationList.as_view(), name='moderation_list'),
    path('create_blog/', BlogsCreateView.as_view(), name='create_blog'),
    path('blog/<int:pk>', BlogsDetailView.as_view(), name='view_blog'),
    path('edit/<int:pk>', BlogsUpdateView.as_view(), name='edit_blog'),
    path('delete/<int:pk>', BlogsDeleteView.as_view(), name='delete_blog'),
]

