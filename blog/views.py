from django.shortcuts import render, redirect
from .models import Category
from django.contrib.auth import authenticate, login, logout
# Create your views here.


def home(request):
    three_category = Category.objects.order_by('id')[:3]
    rest_category = Category.objects.order_by('id')[3:]
    context = {
        'three_category': three_category,
        'rest_category': rest_category,
    }
    return render(request, 'pages/home.html', context)

def userlogout(request):
    logout(request)
    return redirect('home')


# def category_view(request):
#     # categories = Category.objects.all()
#     # print(categories)
#     context = {
#         'categories': categories
#     }
#     return render(request, 'components/header.html', context)