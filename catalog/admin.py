from .models import Qualification, Faculty, Syllabus, Direction, Schoolsubject, Examset, Event, Review, Teacher, WishList
from django.contrib import admin


admin.site.register(Teacher)
admin.site.register(Qualification)
admin.site.register(Faculty)
admin.site.register(Syllabus)
admin.site.register(Direction)
admin.site.register(Schoolsubject)
admin.site.register(Examset)
admin.site.register(Event)
admin.site.register(Review)
admin.site.register(WishList)

