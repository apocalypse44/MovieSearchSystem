from .pickle_handler import load_movies_pickle
import pandas as pd
import re
import requests

def get_posters(recommended_movie_id):
    response = requests.get(f"https://api.themoviedb.org/3/movie/{recommended_movie_id}?api_key=08991b975424d45c942d68a74960feff")
    data = response.json()
    # print(data)
    if 'poster_path' not in data.keys():
        return None
    return (f"https://image.tmdb.org/t/p/w500{data['poster_path']}")

def imdb_id(recommended_movie_id):
    response = requests.get(f"https://api.themoviedb.org/3/movie/{recommended_movie_id}?api_key=08991b975424d45c942d68a74960feff")
    data = response.json()
    # print(data)
    if 'imdb_id' not in data.keys():
        return None
    return (f"https://www.imdb.com/title/{data['imdb_id']}")

def recommend_movie(movie_name):
    movie_name = movie_name.lower()
    movie_name = re.sub(r'\W+', '', movie_name)

    movies, similarity = load_movies_pickle()
    movies_df = pd.DataFrame(movies)
    # data = movies_df['Details'].iloc[0]
    # print(data, similarity[0])
    print(movies_df['name'].isin([movie_name]))
    if movies_df['name'].isin([movie_name]).any():
        index = movies_df[movies_df['name'] == movie_name].index[0]
        # print(index)
        distance = similarity[index]
        recommended_list = sorted(list(enumerate(distance)), key= lambda x: x[1], reverse=True)[1:11]

        recommended_movies = []
        posters = []
        input_movie = []
        imdb_ids = []

        input_movie.append(movie_name)
        input_movie.append(get_posters(movies_df['id'].iloc[index]))
        # print(input_movie)

        for i in recommended_list:
            # print(movies_df['original_title'].iloc[i[0]])
            recommended_movies.append(movies_df['original_title'].iloc[i[0]])
            posters.append(get_posters(movies_df['id'].iloc[i[0]]))
            imdb_ids.append(imdb_id(movies_df['id'].iloc[i[0]]))
        
        if(None in posters):
            index = posters.index(None)
            recommended_movies.pop(index)
            posters.pop(index)

        return recommended_movies, posters, input_movie, imdb_ids
    else:
        return None, None, None, None
