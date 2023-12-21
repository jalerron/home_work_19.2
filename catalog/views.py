from django.shortcuts import render

from catalog.models import Product


def catalog(request):
    products_list = Product.objects.all()
    content = {
        'object_list': products_list,
        'title_head': 'Skystore',
        'title': 'Каталог'
    }

    return render(request, 'catalog/catalog.html', content)


def index(request):

    product_list = Product.objects.filter(is_active=True)
    content = {
        'object_list': product_list,
        'title_head': 'Skystore',
        'title': 'Skystore'
    }
    return render(request, 'catalog/index.html', content)


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'{name} ({phone}): {message}')

    content = {
        'title_head': 'Skystore',
        'title': 'Контакты',
    }

    return render(request, 'catalog/contacts.html', content)


def product_detail(request, product_id):
    products_list = Product.objects.get(pk=product_id)
    content = {
        'object': products_list,
        'title_head': 'Skystore',
        'title': 'Каталог'
    }

    return render(request, 'catalog/product_detail.html', content)

# def view_product(request, pk):
#     product_item = get_object_or_404(Product, pk=pk)
#     context = {
#         'object': product_item,
#     }
#
#     return render(request, 'catalog/product_detail.html', context)
