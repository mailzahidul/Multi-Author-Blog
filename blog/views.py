from django.shortcuts import render, redirect
from .models import Category
from django.views import View
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import Password_Change_Form, EmailSendForm
from django.core.mail import send_mail
# Create your views here.


def home(request):
    return render(request, 'pages/home.html')

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


def change_password(request):
    if request.method == 'POST':
        forms = Password_Change_Form(request.user, request.POST)
        if forms.is_valid():
            forms.save()
            update_session_auth_hash(request, request.user)
            return redirect('change_password_done')
    else:
        forms = Password_Change_Form(request.user)
    context = {
        'forms':forms
    }
    return render(request, 'user/changepassword.html', context)


def change_password_done(request):
    return render(request, 'user/change_password_done.html')


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


def contact_us(request):
    forms = EmailSendForm()
    if request.method == 'POST':
        forms = EmailSendForm(request.POST)
        if forms.is_valid():
            subject = forms.cleaned_data['subject']
            sender = forms.cleaned_data['sender']
            message = forms.cleaned_data['message']
            recipients = ['mailzahidul@gmail.com']
            send_mail(subject, message, sender, recipients)
            if request.user.is_authenticated:
                user = request.user
                obj = forms.save(commit=True)
                obj.sender_user=user
                obj.sender=user.email
                obj.save()
                return redirect('contact_us')
            forms.save()
            return redirect('contact_us')
        else:
            messages.error(request, forms.errors)
    context={
        'forms':forms
    }
    return render(request, 'pages/contact_us.html', context)