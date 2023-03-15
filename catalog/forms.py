from django.contrib.auth.models import User
from django import forms
from . import models

class CommentForm(forms.ModelForm):
    #user = forms.ModelChoiceField(queryset = User.objects.all(), blank = True)
    #direction = forms.ModelChoiceField(queryset = models.Direction.objects.all(), blank = True)
    class Meta:
        model = models.Comment
        fields=("text", "rate" )
 
class ReviewForm(forms.ModelForm):
    #user = forms.ModelChoiceField(queryset = User.objects.all(), blank = True)
    #event = forms.ModelChoiceField(queryset = models.Event.objects.all(), blank = True)
    class Meta:
        model = models.Review
        fields=("comment", "rate" )



