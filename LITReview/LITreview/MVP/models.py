from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.db.models.fields import PositiveSmallIntegerField

from authentication.models import User

# class User(AbstractUser): # temporaire, devra etre modifier lors de la gestion de l'authentification
#     profil_photo = models.ImageField(verbose_name="photo de profil")


class Ticket(models.Model):

    title = models.fields.CharField(max_length=128)
    description = models.fields.CharField(max_length=2048)
    image = models.ImageField(null=True, blank=True)
    time_created = models.fields.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Review(models.Model):

    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    rating = PositiveSmallIntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    headline = models.fields.CharField(max_length=128)
    body = models.fields.TextField(max_length=8192, blank=True)
    time_created = models.fields.DateTimeField(auto_now_add=True)


class UserFollows(models.Model):

    class Meta():
        unique_together = ['user', 'followed_user']

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    followed_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='followed_by')



