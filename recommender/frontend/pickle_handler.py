import pickle
import os

def load_movies_pickle():
    file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'pickles', 'movies.pkl')
    with open(file_path, 'rb') as f:
        movies = pickle.load(f)
    file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'pickles', 'similarity.pkl')
    with open(file_path, 'rb') as f:
        similarity = pickle.load(f)
    return movies, similarity