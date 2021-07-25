from django.shortcuts import render
from .models import Category
# Create your views here.


def home(request):
    categories = Category.objects.all()
    print(categories)
    context = {
        'categories': categories
    }
    return render(request, 'pages/home.html', context)


# def category_view(request):
#     # categories = Category.objects.all()
#     # print(categories)
#     context = {
#         'categories': categories
#     }
#     return render(request, 'components/header.html', context)