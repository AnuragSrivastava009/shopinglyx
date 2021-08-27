from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm,PasswordChangeForm,PasswordResetForm,SetPasswordForm
from django.contrib.auth.models import User


class CustomerRegistrationForm(UserCreationForm):
    password1=forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2=forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    email=forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class':'form-control'}))
    
    class Meta:
        model=User
        fields=['username','email','password1','password2']
        labels ={'email':'Email'}
        widgets ={'username':forms.TextInput(attrs={'class':'form-control'})}
        

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','password1','password2']


class CustomerProfileForm(forms.ModelForm):
    
    class Meta:
        model = Customer
        fields = ["name","locality","state","city","zipcode"]


        