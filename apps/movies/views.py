from django.shortcuts import render
from .models import Movies, Actors
# Create your views here.
def index(request):
    people = Actors.objects.get()
    movies = Movies.objects.get()
    return render(request, 'movies/index.html')
