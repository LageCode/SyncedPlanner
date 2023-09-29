from django import forms
from django.core import validators
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(label_suffix="", *args, **kwargs)


class RegisterForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(label_suffix="", *args, **kwargs)
