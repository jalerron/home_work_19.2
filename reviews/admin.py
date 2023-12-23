from django.contrib import admin

from reviews.models import Reviews

@admin.register(Reviews)
class ReviewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'body', 'date',)
    list_filter = ('product',)
    search_fields = ('name', 'product',)