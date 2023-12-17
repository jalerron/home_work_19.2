from django.core.management import BaseCommand
from catalog.models import Product, Category
from django.core.management import call_command


class Command(BaseCommand):

    def handle(self, *args, **options):
        call_command('dumpdata', 'catalog', output='data.json')
        Product.objects.all().delete()
        Category.objects.all().delete()