from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from catalog.models import Product

from reviews.models import Reviews


class ReviewsCreateView(CreateView):
    model = Reviews
    fields = ('name', 'body', 'product', 'date')
    success_url = reverse_lazy('catalog:index')


class ReviewsListView(ListView):
    model = Reviews
