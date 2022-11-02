from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from blogApp.models import *


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(label="Nombre", max_length=140, required=True)
    email = forms.EmailField(label="Email",required=True)

    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'email',
            'password1',
            'password2',
        )


class UserEditionForm(UserCreationForm):
    email = forms.EmailField(label="Modificar email")
    password1 = forms.CharField(label="Nueva Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)
    first_name = forms.CharField(label="Nombre")

    class Meta:
        model = User
        fields = ["email", "password1", "password2", "first_name"]


class AvatarForm(forms.ModelForm):
    imagen = forms.ImageField()

    class Meta:
        model = Avatar
        fields = ["imagen", "user"]