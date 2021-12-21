from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.db.models.fields import PositiveSmallIntegerField
from PIL import Image

from authentication.models import User


class Ticket(models.Model):
    identity = models.fields.CharField(max_length=100, default="ticket")
    title = models.fields.CharField(max_length=128, verbose_name="Titre")
    description = models.fields.CharField(max_length=2048)
    image = models.ImageField(null=True, blank=True, verbose_name="Image")
    time_created = models.fields.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    answered = models.fields.CharField(max_length=10, default='False')

    IMAGE_MAX_SIZE = (700, 700)

    def resize_image(self):
        image = Image.open(self.image)
        image.thumbnail(self.IMAGE_MAX_SIZE)
        image.save(self.image.path)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.resize_image()


class Review(models.Model):
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

    user = models.ForeignKey(to=settings.AUTH_USER_MODEL,  on_delete=models.CASCADE)
    followed_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='followed_by')

