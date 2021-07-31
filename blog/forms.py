from django import forms
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth.models import User
from .models import EmailSend


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

class Password_Change_Form(PasswordChangeForm):
    old_password = forms.CharField( label='Current Password' , widget=forms.PasswordInput(attrs={'class':'form-control'}))
    new_password1 = forms.CharField(label='New Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    new_password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))


class EmailSendForm(forms.ModelForm):
    class Meta:
        model = EmailSend
        exclude = ['sender_user', 'send_date']
        widgets = {
            'sender' : forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Email'}),
            'subject' : forms.TextInput(attrs={'class':'form-control'}),
            'message' : forms.Textarea(attrs={'class':'form-control'}),
        }