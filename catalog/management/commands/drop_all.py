from django.core.management import BaseCommand
from catalog.models import Product, Category
from django.core.management import call_command


class Command(BaseCommand):

    def handle(self, *args, **options):
        Product.objects.all().delete()
        Category.objects.all().delete()
