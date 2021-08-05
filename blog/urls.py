from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/registration', views.Registration_views.as_view(), name='registration'),
    path('accounts/login/', views.userlogin, name='login'),
    path('accounts/logout/', views.userlogout, name='logout'),
    path('accounts/password_change', views.change_password, name='password_change'),
    path('accounts/password_change/done', views.change_password_done, name='password_change_done'),
    # Password Reset or Password Forget
    # https://docs.djangoproject.com/en/3.0/topics/auth/default/#using-the-views
    path('accounts/reset_password/', auth_views.PasswordResetView.as_view(template_name = "user/reset_password.html"), name ='reset_password'),
    path('accounts/reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name = "user/password_reset_sent.html"), name ='password_reset_done'),
    path('accounts/reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name = "user/password_reset_form.html"), name ='password_reset_confirm'),
    path('accounts/reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name = "user/password_reset_done.html"), name ='password_reset_complete'),
    path('post/view_post/<int:id>', views.view_post, name='view_post'),
    path('contact_us/', views.contact_us, name='contact_us')
]