from django.db import models
from django.urls import reverse 
from django.core.validators import FileExtensionValidator
import os

class Guide (models.Model):
    title = models.CharField (max_length = 200, verbose_name = "Название", help_text = "Введите короткое название гайда")
    template = models.FileField ( 
        verbose_name = "Прикрепить шаблон", 
        upload_to = "guides/templates", 
        validators=[FileExtensionValidator(allowed_extensions=["html"])])

    def __str__ (self):
        return self.title

    def getAbsoluteUrl(self):
        return reverse("guide-details", args=[str(self.id)])

    def filename(self):
        return os.path.basename(self.template.name)



