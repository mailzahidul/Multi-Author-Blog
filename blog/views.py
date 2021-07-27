from django.shortcuts import render, redirect
from .models import Category
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
# Create your views here.


def home(request):
    three_category = Category.objects.order_by('id')[:3]
    rest_category = Category.objects.order_by('id')[3:]
    context = {
        'three_category': three_category,
        'rest_category': rest_category,
    }
    return render(request, 'pages/home.html', context)

class Registration_views(View):
    def get(self, request):
        return render(request, 'user/registration.html')

    def post(self, request):
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if password1 == password2:
            user_check = authenticate(username=username, password=password1)
            if user_check is None:
                try:                    
                    User.objects.create_user(first_name=fname, last_name=lname, email=email, username=username, password=password1)
                    messages.success(request, "Sign Up Successfully.")
                except Exception as errors:
                    messages.error(request, "Username Already Exist.")
            else:
                messages.error(request, "Username Already Exist.")
        else:
            messages.error(request, "Password not match.")
        return render(request, 'user/registration.html')


def userlogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user_obj = authenticate(username=username, password=password)
        if user_obj is not None:
            login(request, user_obj)
            return redirect('home')
        else:
            messages.error(request, "Username or Password Invalid.")
    return render(request, 'user/login.html')



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