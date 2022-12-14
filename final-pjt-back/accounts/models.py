from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser

from imagekit.processors import Thumbnail
from imagekit.models import ProcessedImageField

from movies.models import Movie, Genre, Ott

# Create your models here.
class User(AbstractUser):
    followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')
    collection = models.ManyToManyField(Movie)
    genre_preference = models.ManyToManyField(Genre, related_name='prefer_users', through='Preference')
    using_otts = models.ManyToManyField(Ott, related_name='using_users')
    profile_img = ProcessedImageField(
        blank=True,
        upload_to='profile_imgs/',
        processors=[Thumbnail(240, 240)],
        format='JPEG'
    )


class Preference(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    score = models.IntegerField()
    like = models.BooleanField()