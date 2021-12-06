from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.db.models.fields import PositiveSmallIntegerField

from authentication.models import User

# class User(AbstractUser): # temporaire, devra etre modifier lors de la gestion de l'authentification
#     profil_photo = models.ImageField(verbose_name="photo de profil")


class Ticket(models.Model):
    identity = models.fields.CharField(max_length=100, default="ticket")
    title = models.fields.CharField(max_length=128)
    description = models.fields.CharField(max_length=2048)
    image = models.ImageField(null=True, blank=True)
    time_created = models.fields.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Review(models.Model):

    # ONE_STAR ="one"
    # TWO_STAR ="two"
    # THREE_STAR ="three"
    # FOUR_STAR ="four"
    # FIVE_STAR ="five"

    # RATING_CHOICES = (
    #     (ONE_STAR, 1), 
    #     (TWO_STAR, 2),
    #     (THREE_STAR, 3),
    #     (FOUR_STAR, 4),
    #     (FIVE_STAR, 5),
    # )
    identity = models.fields.CharField(max_length=100, default="review")
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

# Create your models here.
