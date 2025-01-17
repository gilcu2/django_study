from django.shortcuts import render
from .models import Movie


def index(request):
    template_data = {'title': 'Movies', 'movies': Movie.objects.all()}
    return render(request, 'movies/index.html', {'template_data': template_data})


def show(request, id):
    movie = Movie.objects.get(id=id)
    template_data = {'title': movie['name'], 'movie': movie}
    return render(request, 'movies/show.html', {'template_data': template_data})
