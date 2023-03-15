from django.urls import path
from django.views.generic import RedirectView
from django.http import HttpResponseRedirect
from . import views

urlpatterns = [
    path ( "", views.index, name = "index"),
    path ( "#", RedirectView.as_view(url = "")),
    path ( "facults", views.facultsList.as_view(), name = "facults"),
    path ( "faculty/<int:pk>", views.facultyDetails, name = "faculty-details"),
    path ( "directions", views.directionsList.as_view(), name = "directions"),
    path ( "directions/compare/", views.Compare.as_view(), name = "compare"),
    path ( "directions/compare/<int:first>/", views.compareWithFirst, name = "compare-with-first"),
    path ( "directions/compare/<int:first>/<int:second>", views.fullCompare, name = "full-compare"),
    path ( "direction/<int:pk>", views.directionDetails, name = "direction-details"),
    path ( "direction/<int:pk>/comment", views.leaveComment, name = "leave-comment"),
    path ( "events", views.eventsList.as_view(), name = "events"),
    path ( "event/<int:pk>", views.eventDetails, name = "event-details"),
    path ( "about", views.aboutUs, name = "about-us"),
    path ( "admission", views.admission, name = "how-to-admission" ),
    ]
