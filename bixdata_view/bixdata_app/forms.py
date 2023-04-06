from django import forms
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=64)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)


class ProfilePicForm(forms.Form):
    profile_pic = forms.ImageField(label='Profile Picture')

