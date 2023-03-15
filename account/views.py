from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse

from django.forms.formsets import formset_factory

import datetime

# Create your views here.

from catalog.models import Event, Review, WishList
from multi_form_view import MultiModelFormView

from . import services
from . import models
from . import forms

def forbidden ( request ):
    return render ( request, "forbidden.html", context = {} )

def signin (request):
    form = forms.SigninAbiturientForm
    if request.method == "POST":
        form = forms.SigninAbiturientForm (request.POST)
        if not form.is_valid() or not services.signin(form): form.add_error(None, "Ошибка регистрации")
        return HttpResponseRedirect(reverse("login"))

    return render (request, "signin.html", context = {"form": form, })
# Create your views here.
class SigninTeacher(MultiModelFormView):
   form_classes = {
      'student_form' : forms.SigninAbiturientForm,
      'teacher_form' : forms.SigninTeacherForm,
   }
   template_name = 'teacher-signin.html'
   def get_success_url(self):
      return reverse('login')
   def forms_valid(self, forms):
      user = forms['student_form'].save()
      print (user)
      if user:
        teacher = forms['teacher_form'].save(commit=False)
        teacher.user = user
        teacher.save()
      return super(SigninTeacher, self).forms_valid(forms)

def signinTeacherTest (request):
    if request.method == "POST":
        form = forms.SigninAbiturientForm (request.POST) 
        formset = forms.SigninTeacherForm (request.POST) 
        if request.POST["password"] == request.POST["repassword"]:
            if all([form.is_valid(),]): 
                print ("form valid")
                user = services.signin(form)
                if user:
                    request.POST._mutable = True
                    request.POST["user"] = f'{user.pk}'
                    request.POST._mutable = False  
                    formset = forms.SigninTeacherForm (request.POST) 
                    if formset.is_valid():
                        formset.save()
                        return HttpResponseRedirect(reverse("login"))
    else:
        form = forms.SigninAbiturientForm() 
        formset = forms.SigninTeacherForm () 


    return render (request, "teacher-signin.html", context = {"form": form, "formset": formset})

def login ( request ):
    form = forms.LoginForm
    if request.method == "POST":
        form = forms.LoginForm (request.POST)
        if form.is_valid():
            if services.login ( request, **form.cleaned_data ): return HttpResponseRedirect(reverse("profile"))
            form.add_error(None, "Неправильное имя и/или пароль")
    return render (request, "login.html", context = {"form": form, })

def logout (request):
    if services.logout ( request ): return render ( request, "logout.html" )
    return render ( request, "logout.html", context = {"error": True} )

def teacher (request):
    if request.method == "POST":
        pass
    eventList = Event.objects.all().filter (owner__pk = request.user.pk)
    context = { "eventList": [] }
    for event in eventList:
        reviews = Review.objects.filter ( event__pk = event.pk )
        context["eventList"].append ( {"place": event, "reviews": reviews} )
    return render ( request, "teacher.html", context = {"placesList": eventList} )

def abiturient (request): 
    if request.method == "POST":
        pass

    wishList = WishList.objects.filter (users__pk=request.user.pk)            
    return render ( request, "abiturient.html", context = {"wishList": wishList} )

@services.login_required
def profile (request):

    try:
        group = request.user.groups.all()[0]
    except:
        return render ( request, "account.html", context = {} )

    if group.name == "abiturient":
        return abiturient ( request )
    if group.name == "teacher":
        return teacher ( request )

    return render ( request, "account.html", context = {} )

@services.login_required
def editProfile (request):
   return render ( request, "editProfile.html", context = {} )

def resetPassword (request):
    pass
