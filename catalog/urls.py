from django.urls import path
from django.views.generic import RedirectView
from django.http import HttpResponseRedirect
from . import views

urlpatterns = [
    path ( "", views.index, name = "index"),
    path ( "#", RedirectView.as_view(url = "")),
    ]
