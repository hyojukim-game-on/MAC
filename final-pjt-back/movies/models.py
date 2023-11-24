from django.db import models
from django.conf import settings

# Create your models here.py

class Movie(models.Model):
    title = models.CharField(max_length=100, null=True)
    release_date = models.DateField( null=True)
    overview = models.TextField( null=True)
    poster_path = models.CharField(max_length=200,  null=True)
    adult = models.BooleanField( null=True)
    genre_ids = models.TextField( null=True)
    popularity = models.FloatField(null=True)