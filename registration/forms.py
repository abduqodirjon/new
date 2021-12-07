from django.db.models import fields
from django.forms import ModelForm, forms
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser


class CustomCreateUserForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = [ 'u_fio', 'guruhi', 'm_fio', 'username', 'tel', 'manzil', 'password1', 'password2']
        # fields = ['username']
    
class CustomUserChangeForm(UserChangeForm):
    password = None
    class Meta:
        model = CustomUser
        fields = ['u_fio', 'guruhi', 'm_fio', 'username', 'tel', 'email', 'manzil', 'image' ]