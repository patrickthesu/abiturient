from django.urls import path
from django.views.generic import RedirectView
from django.http import HttpResponseRedirect
from . import views

urlpatterns = [
    path ( "#", views.profile, name = "profile"),
    path ( "", RedirectView.as_view(url = "#")),
    path ( "login/", views.login, name = "login" ),
    path ( "signin", views.signin, name = "signin" ),
    path ( "signin/teacher/", views.SigninTeacher.as_view(), name = "teacher-signin" ),
    path ( "logout/", views.logout, name = "logout" ),
    path ( "password-reset/", views.resetPassword, name = "reset-password" ),
    path ( "forbidden/", views.forbidden, name = "forbidden" ),
    path ( "edit/", views.editProfile, name = "edit-profile" ),
    ]
