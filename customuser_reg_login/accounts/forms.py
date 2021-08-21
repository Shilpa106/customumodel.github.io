from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# from django.contrib.auth import get_user_model
from django import forms
from .models import CompanyCustomUser


class RegisterForm(UserCreationForm):
    class Meta:
        # model = get_user_model()
        model = CompanyCustomUser
        fields = ['name','username', 'email', 'password1', 'password2','website','phone','address','state','country']


        # fields = ('email', 'username', 'password1', 'password2')


class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Email / Username')
