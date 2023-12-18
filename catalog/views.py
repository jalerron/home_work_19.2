from django.shortcuts import render

from catalog.models import Product


def home(request):
    products_list = Product.objects.all()
    content = {
        'object_list': products_list
    }

    return render(request, 'main/home.html', content)


# def home(request):
#     return render(request, 'main/home.html')


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'{name} ({phone}): {message}')

    return render(request, 'main/contacts.html')
