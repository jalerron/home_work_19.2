from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from catalog.models import Product

from reviews.models import Reviews


class ReviewsCreateView(CreateView):
    model = Reviews
    fields = ('name', 'body', 'product',)
    success_url = reverse_lazy('reviews:list_reviews')


class ReviewsListView(ListView):
    model = Reviews


class ReviewDetailView(DetailView):
    model = Reviews


class ReviewUpdateView(UpdateView):
    model = Reviews
    fields = ('name', 'body', 'date')
    success_url = reverse_lazy('reviews:list_reviews')


class ReviewDeleteView(DeleteView):
    model = Reviews
    success_url = reverse_lazy('reviews:list_reviews')
