import json
from tmdbv3api import TMDb
from tmdbv3api import Movie

tmdb = TMDb()
tmdb.api_key = 'c903b735b0a2fb0e7df0f76312d6109f'

movie = Movie()


def cookie(request):
    try:
        cart = json.loads(request.COOKIES['cart'])
    except:
        cart = []

    print(cart)
    order = []
    items = []

    for i in cart:
        movie_id = cart[i]['id']

        print(movie_id)
        m = movie.details(movie_id)

        item = {
            'movie': m.title,
            'year': m.release_date,
            'id': m.id,

        }

        items.append(item)
    return {'items': items, 'order': order}
