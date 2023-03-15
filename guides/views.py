from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.views import generic

from .models import Guide

class guidesList (generic.ListView):
    model = Guide
    context_object_name = "guides"
    template_name = "guides-list.html"

def guideView (request, pk):
    guide = get_object_or_404 (Guide, pk=pk)
    return render (request, guide.filename(), context = {"guide": guide})
