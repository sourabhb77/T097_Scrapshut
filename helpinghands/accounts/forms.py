from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class CustomUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','first_name','email','password1','password2','is_staff']