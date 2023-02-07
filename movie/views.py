from django.shortcuts import render
from .models import Movie

def homepage(request):
    movie = Movie.objects.filter(draft=True)
    movie_ci = Movie.objects.filter(draft=False)
    context = {
        'movie':movie,
        'movie_ci':movie_ci,
    }
    return render(request, 'index.html', context)
