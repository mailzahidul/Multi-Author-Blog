from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# class RegistrationForm(UserCreationForm):
#     fname = forms.CharField(label="First Name", widget=forms.TextInput(attrs={'class':'form-control'}))
#     lname = forms.CharField(label="Last Name", widget=forms.TextInput(attrs={'class':'form-control'}))
#     password1 = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={'class':'form-control'}))
#     password2 = forms.PasswordInput(label="Confirm Password", widget=forms.PasswordInput(attrs={'class':'form-control'}))
#     email = forms.EmailField(label="Email", widget=forms.EmailInput(attrs={'class':'form-control'}))
#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password1', 'password2']
#         widgets= {
#             username:forms.TextInput(attrs={'class':'form-control'})
#         }