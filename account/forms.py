from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django import forms

class SigninAbiturientForm (forms.Form):
    first_name = forms.CharField(max_length=255, label = "Имя") 
    last_name = forms.CharField(max_length=255, label = "Фамилия") 
    username = forms.CharField(max_length=255, label = "Имя пользователя")
    password = forms.CharField(max_length=255, label = "Пароль", widget=forms.PasswordInput())
    repassword = forms.CharField(max_length=255, label = "Повторите пароль", widget=forms.PasswordInput())
    email = forms.EmailField()
    group = forms.ModelChoiceField(queryset = Group.objects.all())

class SigninTeacherForm (forms.Form):
    patronymic = forms.CharField(max_length=255, label = "Отчество") 
    description = forms.CharField(max_length = 500, label = "О себе", widget = forms.Textarea)

class LoginForm (forms.Form):
    username = forms.CharField(max_length=255, label = "Имя пользователя")
    password = forms.CharField(max_length=255, label = "Пароль", widget=forms.PasswordInput())
