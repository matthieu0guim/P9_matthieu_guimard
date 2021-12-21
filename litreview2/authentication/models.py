from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser): # temporaire, devra etre modifier lors de la gestion de l'authentification
    profil_photo = models.ImageField(verbose_name="photo de profil")
    follows = models.ManyToManyField('self', verbose_name='suit')