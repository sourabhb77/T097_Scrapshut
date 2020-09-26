from django import forms
from .models import NGO_admin
class UserForm(forms.ModelForm):
    class Meta:
        model = NGO_admin
        widgets = {
        'password': forms.PasswordInput(),
    }