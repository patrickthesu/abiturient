from django.contrib.auth.models import User 
from django.urls import reverse 
from django.db import models

from django.core.validators import FileExtensionValidator

class Teacher (models.Model):
    patronymic = models.CharField (max_length = 200, verbose_name = "Отчество", null = True)
    description = models.TextField(max_length = 500, verbose_name = "О себе")
    user = models.ForeignKey(to = User, on_delete = models.CASCADE)
    directions = models.ManyToManyField("Direction", blank = True)

    def __str__ (self):
        return f"{self.user.first_name} {self.user.last_name} {self.patronymic}"

class Qualification(models.Model):
    name = models.CharField (max_length = 200, verbose_name = "Квалификация")

    def __str__ (self):
        return str(self.name)

class Faculty(models.Model):
    name = models.CharField (max_length = 200, verbose_name = "Название факультета")
    description = models.TextField (max_length = 2000, verbose_name = "Описание")
    dean = models.ForeignKey ( Teacher, on_delete = models.SET_NULL, null = True)
    adres = models.CharField (max_length = 255, verbose_name = "Адрес")
    phone = models.CharField (max_length = 12, verbose_name = "Телефон")
    email = models.EmailField (max_length=255 )

    def __str__(self):
        return str(self.name)

    def getAbsoluteUrl(self):
        return reverse("faculty-details", args=[str(self.id)])


class Syllabus(models.Model):
    file = models.FileField ( 
        verbose_name = "Прикрепить учебный план", 
        upload_to = "media/documents/syllabs", 
        validators=[FileExtensionValidator(allowed_extensions=['dot', "docx", "doc", "pdf"])])

class Direction(models.Model):
    name = models.CharField (max_length = 200, verbose_name = "Название факультета")
    description = models.TextField (max_length = 2000, verbose_name = "Описание") 
    #intramural = models.BooleanField (default = True, verbose_name = "Очное обучение")
    price = models.DecimalField (max_digits = 8, decimal_places = 2, verbose_name = "Цена")
    budgets = models.PositiveIntegerField ( verbose_name = "Количестов бюджетных мест" )
    payed = models.PositiveIntegerField ( verbose_name = "Количестов платных мест" )
    years = models.PositiveIntegerField (verbose_name = "Срок обучения ")
    ofline = models.BooleanField (default = True, verbose_name = "Есть очные группы")
    online = models.BooleanField (default = False, verbose_name = "Есть заочные группы")
    curator = models.ForeignKey(Teacher, on_delete = models.SET_NULL, null = True, verbose_name = "", related_name = "curator")
    syllabus = models.ForeignKey(Syllabus, on_delete = models.SET_NULL, null = True)
    qualification = models.ForeignKey (Qualification, on_delete = models.CASCADE)
    faculty = models.ForeignKey(to = Faculty, on_delete = models.CASCADE)
    
    def __str__ (self):
        return f"{self.name} {self.price}"

    def getAbsoluteUrl(self):
        return reverse("direction-details", args=[str(self.id)])




class Schoolsubject(models.Model):
    name = models.CharField (max_length = 200)
    def __str__ (self):
        return f"{self.name}"


class Examset(models.Model):
    mark = models.PositiveIntegerField ( verbose_name = "Минимальная оценка" )
    subject = models.ForeignKey(Schoolsubject, on_delete = models.CASCADE)
    direction = models.ForeignKey(Direction, on_delete = models.CASCADE)
    required = models.BooleanField (default = True, verbose_name = "Обязательный экзамен")
    def __str__ (self):
        return f"Екзамены для {self.direction.name}"


class Event(models.Model):
    title = models.CharField (max_length = 200, verbose_name = "Название", help_text = "Введите короткое название вашего мероприятия")
    description = models.TextField ( max_length = 2000, verbose_name = "Описание", help_text = "Введите описание вашего мероприятия. Укажите чего стоит ожидать посетителям, сколько это займет по времени и как вы собираетесь проводить время на этом этапе." )
    required = models.BooleanField ( default = True, verbose_name = "Регистрация обязательна" )
    online = models.BooleanField ( default = True, verbose_name = "Это онлайн встреча?" )
    place = models.CharField (max_length = 200, verbose_name = "Адрес", help_text = "Введите адрес проведения (можно ссылку).")
    owner = models.ForeignKey(Teacher, on_delete = models.CASCADE)
    
    
    def getAbsoluteUrl(self):
        return reverse("event-details", args=[str(self.id)])

    def __str__ (self):
        return f"{self.title}"
 
RATE_CHOISES = [
        (1, "Ужасно"),
        (2, "Плохо"),
        (3, "Удовлетворительно"),
        (4, "Хорошо"),
        (5, "Отлично"),
        ]

class Comment(models.Model):
    direction = models.ForeignKey (to = Direction, on_delete = models.CASCADE)
    text = models.TextField ( verbose_name = "Коментарий", max_length = 1000)
    rate = models.PositiveSmallIntegerField( verbose_name = "Оценка", choices=RATE_CHOISES )
    user = models.ForeignKey ( User, on_delete = models.CASCADE)

    def __str__ (self):
        return f"{self.text} | {self.user.first_name} {self.user.last_name}"

class Review(models.Model):
    comment = models.TextField ( verbose_name = "Коментарий", max_length = 1000)
    rate = models.PositiveSmallIntegerField( verbose_name = "Оценка", choices=RATE_CHOISES )
    event = models.ForeignKey (to = Event, on_delete = models.CASCADE)
    user = models.ForeignKey ( User, on_delete = models.CASCADE)
    def __str__ (self):
        return f"{self.comment} | {self.user.first_name} {self.user.last_name}"

class WishList (models.Model):
    user = models.ForeignKey(to = User, on_delete = models.CASCADE, related_name = "creator")
    direction = models.ForeignKey(to = User, on_delete = models.CASCADE)

    def __str__ (self):
        return str(self.user)

