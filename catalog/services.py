from django.conf import settings
from django.core.cache import cache

from catalog.models import Category


def get_category_cache():
    key = 'category_list'
    category_list = cache.get(key)
    if category_list is None:
        category_list = Category.objects.all()
        cache.set(key, category_list)
    return category_list


# def get_version(context):
#     for product in context['object_list']:
#         active_version = product.version_set.filter(is_active=True).first()
#
#         if active_version:
#             product.active_version_number = active_version.num_version
#             product.active_version_name = active_version.name
#         else:
#             product.active_version_number = None
#             product.active_version_name = None
