from django.shortcuts import render, redirect
from django.http import HttpResponse
from .recommend import recommend_movie
import pandas as pd



# Create your views here.
def splash(request):
    return render(request, 'splash.html')

def home(request):
    return render(request, 'home.html') 

def next(request):
    recommendations = []
    posters = []
    imdb_ids = []
    if request.method == 'POST':
        movie_name = request.POST.get('movie_name')
        print(movie_name)
        if movie_name == "":
            return redirect('home')

        recommendations, posters, input_movie, imdb_ids = recommend_movie(movie_name)
        if recommendations == None:
            return redirect('home')
        
        zipped_list = zip(recommendations, posters, imdb_ids)
    return render(request, 'hey.html', {'recommendations':list(zipped_list), 'input_movie': input_movie})