from tmdbv3api import TMDb
from tmdbv3api import Movie

tmdb = TMDb()
tmdb.api_key = 'c903b735b0a2fb0e7df0f76312d6109f'


def popular_movies(request):
    movie = Movie()
    popular = movie.popular()
    trailers = []
    keys = []

    products=[]

    for p in popular:
        videos = movie.videos(p.id)
        trailers.append(videos)



    for t in trailers:
        for i in t:
            video_key = i.key
    product = {
        'title': p.title,
        'poster_path': p.poster_path,
        'backdrop_path': p.backdrop_path,
        'duration': p.runtime,
        'year': p.release_date,
        'video': video_key,
    }


    return keys
