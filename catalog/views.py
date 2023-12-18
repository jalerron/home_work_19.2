from django.shortcuts import render

from catalog.models import Product


def catalog(request):
    products_list = Product.objects.all()
    content = {
        'object_list': products_list,
        'title_head': 'Skystore',
        'title': 'Каталог'
    }

    return render(request, 'main/home.html', content)


def index(request):
    content = {
        'title_head': 'Skystore',
        'title': 'Skystore'
    }
    return render(request, 'main/index.html', content)


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

    return render(request, 'main/contacts.html', content)
