from django import forms
from .models import NGO
class UserForm(forms.ModelForm):
    class Meta:
        model = NGO
        widgets = {
        'password': forms.PasswordInput(),
    }