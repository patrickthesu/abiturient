from django.contrib.auth.models import User
from django.db import models

class Message (models.Model):
    sender = models.ForeignKey(to = User, on_delete = models.CASCADE, related_name = "sender", blank = True)
    reciever = models.ForeignKey(to = User, on_delete = models.CASCADE, related_name = "reciever", verbose_name = "Кому")
    text = models.TextField(max_length = 500, verbose_name = "Текст сообщения")
    time = models.ForeignKey(to = User, on_delete = models.CASCADE, verbose_name = "Отправлено")
