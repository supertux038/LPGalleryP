from django.contrib.auth.models import AbstractUser
from django.db import models

from LPGallery import settings


class Role(models.Model):
    NAMES = (
        ('Ю', 'Юзер'),
        ('М', 'Модератор'),
        ('А', 'Админ')
    )
    name = models.CharField(max_length=1, choices=NAMES)

    def __str__(self):
        return self.get_name_display()


class User(AbstractUser):

    avatar_photo = models.ImageField(upload_to=settings.USER_AVATAR_DIRECTORY, blank=True,
                                     default=settings.USER_AVATAR_DIRECTORY+'/default.png', null=True)
    roles = models.ManyToManyField(Role)
    info = models.TextField(max_length=300, blank=True, null=True)

    def get_roles(self):
        return list(self.roles.all())

    def is_admin(self):
        return Role(name='A') in list(self.roles.all())

    # def get_models(self):
    #     return LPModel.objects.filter(author=self)

    class Meta:
        ordering = [
            '-username'
        ]

