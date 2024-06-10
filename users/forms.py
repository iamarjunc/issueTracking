from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import CustomUser


class CreateUserForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username','email','password1','password2','user_type']