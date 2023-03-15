from django.urls import path
from django.views.generic import RedirectView
from django.http import HttpResponseRedirect
from . import views

urlpatterns = [
    path ( "", views.guidesList.as_view(), name = "guides-list"),
    path ( "<int:pk>", views.guideView, name = "guide-details"),
    ]
