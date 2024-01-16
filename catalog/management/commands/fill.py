from django.core.management import BaseCommand
from catalog.models import Product, Category
from blogs.models import Blogs
from django.core.management import call_command


class Command(BaseCommand):

    def handle(self, *args, **options):
        Product.objects.all().delete()
        Category.objects.all().delete()
        Blogs.objects.all().delete()

        call_command('loaddata', 'data.json')
