from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/registration', views.Registration_views.as_view(), name='registration'),
    path('accounts/login/', views.userlogin, name='login'),
    path('accounts/logout/', views.userlogout, name='logout'),
    path('contact_us/', views.contact_us, name='contact_us')
]