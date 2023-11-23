from django.db import models
from django.conf import settings

# Create your models here.py

class Movie(models.Model):
    title = models.CharField(max_length=100)
    release_date = models.DateField()
    overview = models.TextField()
    poster_path = models.CharField(max_length=200)
    adult = models.BooleanField()
    genre_ids = models.TextField()