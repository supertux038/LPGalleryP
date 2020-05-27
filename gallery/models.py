import os

from django.contrib.auth.models import AbstractUser
from django.core.validators import FileExtensionValidator
from django.db import models
from django.conf import settings

from django.utils import timezone

from security.models import User


class LPModel(models.Model):
    DIFFICULTIES = (
        ('Н', 'Неоцененный'),
        ('Л', 'Легкий'),
        ('С', 'Средний'),
        ('Т', 'Тяжелый')
    )
    CATEGORIES = (
        ('Т', 'Транспорт'),
        ('О', 'Общее'),
        ('Л', 'Ландшафт'),
        ('П', 'Персонажи'),
    )

    author = models.ForeignKey('security.User', on_delete=models.CASCADE)
    name = models.CharField(max_length=20, unique=True)
    description = models.CharField(max_length=400)
    small_description = models.CharField(max_length=40)
    file = models.FileField(upload_to=settings.USER_MODEL_DIRECTORY, default=settings.USER_MODEL_DIRECTORY+'404.babylon',
                            blank=False, null=False)
    video_lesson_link = models.URLField(max_length=100, blank=True)
    image = models.ImageField(upload_to=settings.USER_MODEL_IMAGE_DIRECTORY,
                              default=settings.USER_MODEL_IMAGE_DIRECTORY+'/default.jpg', blank=False,
                              validators=[FileExtensionValidator(allowed_extensions=['jpg', 'png'])])
    main_page = models.ForeignKey('MainPage', on_delete=models.CASCADE, blank=True, null=True)
    difficulty = models.CharField(max_length=1, choices=DIFFICULTIES)
    category = models.CharField(max_length=1, choices=CATEGORIES)

    def __str__(self):
        return self.name

    def filename(self):
        return os.path.basename(self.file.name)

    class Meta:
        ordering = [
            '-author',
            '-name',
            '-difficulty',
            '-category'
        ]
        verbose_name = 'LowPoly Model'
        verbose_name_plural = 'LowPoly Models'


class MainPage(models.Model):
    name = models.CharField(max_length=20)
    created_time = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=40)
    text = models.CharField(max_length=300)

    def get_models(self):
        return LPModel.objects.filter(main_page=self)

    def __str__(self):
        return self.name

    class Meta:
        ordering = [
            '-title',
            '-name',
            '-text',
            '-created_time'
        ]


class Community(models.Model):
    title = models.CharField(max_length=20)
    description = models.CharField(max_length=100)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+')
    avatar_photo = models.ImageField(upload_to=settings.USER_AVATAR_DIRECTORY, blank=True,
                                     default=settings.USER_AVATAR_DIRECTORY+'default.png', null=True)
    users = models.ManyToManyField('security.User')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Communities'


class Comment(models.Model):
    on_model = models.ForeignKey('LPModel', on_delete=models.CASCADE, null=True)
    author = models.ForeignKey('security.User', on_delete=models.CASCADE)
    text = models.CharField(max_length=100)
    creation_time = models.DateTimeField()

    class Meta:
        ordering = ['creation_time']

    def __str__(self):
        return '%s on %s' % (self.author, self.creation_time.date())


# class Lesson(models.Model):

