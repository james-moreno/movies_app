from django.db import models

# Create your models here.
class Movies(models.Model):
    movie_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Actors(models.Model):
    actor_name = models.CharField(max_length=255)
    movies = models.ManyToManyField(Movies)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
