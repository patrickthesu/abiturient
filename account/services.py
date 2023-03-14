from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib import auth 

def login_required (functionToDecorate):
    def wrapper (request, *args, **kwargs):
        if not request.user.is_authenticated: return HttpResponseRedirect(reverse("login"))
        return functionToDecorate(request, *args, **kwargs)
    return wrapper

def group_required (functionToDecorate, group = "consumer"):
    def wrapper (request, *args, **kwargs):
        for g in request.user.groups.all():
            if group in g.name: return  functionToDecorate(request, *args, **kwargs)
        return HttpResponseRedirect (reverse("forbidden"))
    return wrapper

def signin (filledForm):
    try:
        group = filledForm.cleaned_data["group"]
        del (filledForm.cleaned_data["repassword"])
        del (filledForm.cleaned_data["group"])
        user = User.objects.create_user(**filledForm.cleaned_data)
        group.user_set.add(user)
        return user
    except Exception as err:
        print (err)
        return False

def login ( request, username, password ):
    print (f"Username: '{username}' password: '{password}'")
    user = auth.authenticate(request, username = username, password = password)
    if user is not None: 
        auth.login (request, user)
        return True
    return False

def logout ( request ):
    try: 
        auth.logout (request)
        return True
    except Exception as err:
        print ( "ERROR: Logout " + str (err) )
        return False
