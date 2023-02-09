from django.shortcuts import render
from .models import Movie, News, Settings, Contact
from django.views.generic import View

def homepage(request):
    setting = Settings.objects.latest('id') 
    movie = Movie.objects.filter(draft=True)
    news = News.objects.all()
    news_com = News.objects.filter(genre=2)
    movie_ci = Movie.objects.filter(draft=False)
    context = {
        'movie':movie,
        'movie_ci':movie_ci,
        'news':news,
        'setting':setting,
        'news_com':news_com,
    }
    return render(request, 'index.html', context)


def contact(request):
    setting = Settings.objects.latest('id')  
    contact = Contact.objects.latest('id')  
    context = {  
        'setting':setting, 
        'contact':contact, 
    }
    return render(request, 'contact.html', context)


class NewsDetailView(View):
    def get(self, request, slug):
        setting = Settings.objects.latest('id') 
        news = News.objects.get(slug=slug)
        context = {
            'setting':setting, 
            'news':news
        }
        return render(request, 'news.html', context)


class MovieDetailView(View):
    def get(self, request, slug):
        setting = Settings.objects.latest('id') 
        movie = Movie.objects.get(slug=slug)
        context = {
            'setting':setting, 
            'movie':movie
        }
        return render(request, 'single_movie.html', context)