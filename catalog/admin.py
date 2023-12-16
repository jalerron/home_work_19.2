from django.contrib import admin

from catalog.models import Product, Category


# admin.site.register(Product)
# admin.site.register(Category)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price_for_one', 'description',)
    list_filter = ('category',)
    search_fields = ('name', 'description',)
