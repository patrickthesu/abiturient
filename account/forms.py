from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django import forms

from catalog.models import Teacher
from . import services

from django import forms

class SigninAbiturientForm(forms.ModelForm):
    password = forms.CharField(max_length=255, label = "Пароль", widget=forms.PasswordInput())
    repassword = forms.CharField(max_length=255, label = "Повторите пароль", widget=forms.PasswordInput())
    group = forms.ModelChoiceField(queryset = Group.objects.all(), blank = True)

    class Meta:
        model=User
        fields=("first_name", "last_name", "username", "password", "repassword", "email" )
        labels={"first_name": "Имя", "last_name": "Фамилия", "username": "Имя пользователя", "password": "Пароль", "repassword": "Повторите пароль", "email": "Email"}

    def clean(self):
        #run the standard clean method first
        cleaned_data=super(SigninAbiturientForm, self).clean()
        password = cleaned_data.get("password")
        password_verify = cleaned_data.get("repassword")

        #check if passwords are entered and match
        if password and password_verify and password==password_verify:
            print ("pwd ok")
        else:
            raise forms.ValidationError("Passwords do not match!")

        #always return the cleaned data
        return cleaned_data

    def save(self, commit=True):
        user = super(SigninAbiturientForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user    


class SigninTeacherForm(forms.ModelForm):
   class Meta:
      model=Teacher
      fields=("patronymic", "description")
    
class SigninAbiturientFormTest (forms.Form):
    first_name = forms.CharField(max_length=255, label = "Имя") 
    last_name = forms.CharField(max_length=255, label = "Фамилия") 
    username = forms.CharField(max_length=255, label = "Имя пользователя")
    password = forms.CharField(max_length=255, label = "Пароль", widget=forms.PasswordInput())
    repassword = forms.CharField(max_length=255, label = "Повторите пароль", widget=forms.PasswordInput())
    email = forms.EmailField()
    group = forms.ModelChoiceField(queryset = Group.objects.all())

class SigninTeacherFormTest (forms.Form):
    class Meta:
        model = Teacher
        fields = '__all__'
    #patronymic = forms.CharField(max_length=255, label = "Отчество") 
    #description = forms.CharField(max_length = 500, label = "О себе", widget = forms.Textarea)

class LoginForm (forms.Form):
    username = forms.CharField(max_length=255, label = "Имя пользователя")
    password = forms.CharField(max_length=255, label = "Пароль", widget=forms.PasswordInput())
