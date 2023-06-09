from django.views import generic
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse

from django.db.models import Q


from . import forms
from . import models

def index (request):    
    return render (request, "base-generic.html", context = {})

def aboutUs (request):
    return render (request, "about.html")

def admission (request):
    return render (request, "admission.html")

def leaveComment (request, pk):
    direction = get_object_or_404 (models.Direction, pk=pk)
    form = forms.CommentForm
    if request.method == "POST":
        request.POST._mutable = True
        request.POST["user"] = f'{request.user.pk}'
        request.POST["direction"] = f"{pk}"
        request.POST._mutable = False   
        form = forms.CommentForm (request.POST) 
        if form.is_valid(): 
            form.save()
            return HttpResponseRedirect(reverse("direction-details"), args=[pk])

    return render (request, "leave-comment.html", context = {"form": form, "direction": direction })


class facultsList (generic.ListView): 
    model = models.Faculty
    context_object_name = "facults_list"
    template_name = "facults-list.html"

def facultyDetails (request, pk):
    faculty = get_object_or_404 (models.Faculty, pk=pk)
    directions = models.Direction.objects.filter (faculty__pk = pk)
    
    return render ( request, "faculty-details.html", context = {"faculty": faculty, "directions": directions, "directions_count": directions.count(), "abiturient": True} )


class directionsList (generic.ListView):
    model = models.Direction
    context_object_name = "directions"
    template_name = "direction-list.html"

def directionDetails (request, pk):
    direction = get_object_or_404 (models.Direction, pk=pk)
    comments = models.Comment.objects.filter (direction__pk = pk)
    
    return render ( request, "direction-details.html", context = {"direction": direction, "comments": comments, "directions_count": comments.count()} )

class Compare (generic.ListView):
    model = models.Direction
    context_object_name = "directions"
    template_name = "compare.html"

def compareWithFirst (request, first): 
    firstobject = get_object_or_404 (models.Direction, pk = first)
    directions = models.Direction.objects.filter (~Q(pk=first))
    return render (request, "compare.html", context = {"first": firstobject, "directions": directions})

def fullCompare (request, first, second): 
    firstobject = get_object_or_404 (models.Direction, pk = first)
    secondobject = get_object_or_404 (models.Direction, pk = second)
    return render (request, "compare.html", context = {"first": firstobject, "second": secondobject, })

class eventsList (generic.ListView):
    model = models.Event
    context_object_name = "events"
    template_name = "events-list.html"


def eventDetails (request, pk):
    event = get_object_or_404 (models.Event, pk=pk)
    reviews = models.Review.objects.filter (event__pk = pk)

    form = forms.ReviewForm
    if request.method == "POST":
        form = forms.ReviewForm (request.POST) 
        if form.is_valid(): 
            form.user = f"{request.user.pk}"
            form.event = f"{event.id}"
            form.clean()
            form.save()

    return render ( request, "event-details.html", context = {"event": event, "reviews": reviews , "form": form} )
