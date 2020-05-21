from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings

from django.utils import timezone


class Role(models.Model):
    NAMES = (
        ('U', 'User'),
        ('M', 'Moderator'),
        ('A', 'Admin')
    )
    name = models.CharField(max_length=1, choices=NAMES)

    def __str__(self):
        return self.get_name_display()


class User(AbstractUser):

    avatar_photo = models.ImageField(upload_to=settings.USER_AVATAR_DIRECTORY, blank=True,
                                     default=settings.USER_AVATAR_DIRECTORY+'/default.png', null=True)
    roles = models.ManyToManyField(Role)

    def get_roles(self):
        return self.roles.all()

    def is_admin(self):
        return Role(name='A') in list(self.roles.all())

    class Meta:
        ordering = [
            '-username'
        ]


class LPModel(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=100)
    small_description = models.CharField(max_length=40)
    file = models.FileField(upload_to=settings.USER_MODEL_DIRECTORY, default=settings.USER_MODEL_DIRECTORY+'404.babylon',
                            blank=False, null=False)
    video_lesson_link = models.CharField(max_length=40, blank=True)
    image_path = models.CharField(max_length=40)
    # todo think over next fields
    difficulty = models.CharField(max_length=10)
    category = models.CharField(max_length=10)


class MainPage(models.Model):
    title = models.CharField(max_length=20)
    text = models.CharField(max_length=30)


class Community(models.Model):
    title = models.CharField(max_length=20)
    description = models.CharField(max_length=100)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+')
    avatar_photo = models.ImageField(upload_to=settings.USER_AVATAR_DIRECTORY, blank=True,
                                     default=settings.USER_AVATAR_DIRECTORY+'default.png', null=True)
    users = models.ManyToManyField(User)
