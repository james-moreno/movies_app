from django.shortcuts import render
from .models import Movies, Actors

# Create your views here.
def index(request):

    return render(request, 'movies/index.html')

def add_movie(request):
    pass


def add_actor(request):
    pass


def view_movie(request):
    pass


def view_actor(request):
    pass
