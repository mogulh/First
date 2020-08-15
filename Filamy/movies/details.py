from tmdbv3api import TMDb, TV
from tmdbv3api import Movie

tmdb = TMDb()
tmdb.api_key = 'c903b735b0a2fb0e7df0f76312d6109f'

movie = Movie()
popular = movie.popular()

items = []


def popular_movies(request):
    for p in popular:
        details = movie.details(p.id)
        key = get_video(p.id)

        genres = details.genres
        for g in genres:
            gen = g.get('name')

        title = details.title
        year = details.release_date[:4]
        time = details.runtime
        desc = details.overview
        poster = p.poster_path
        back = p.backdrop_path
        v_key = key
        id = p.id

        item = {
            'title': title,
            'year': year,
            'time': time,
            'desc': desc,
            'poster': poster,
            'back': back,
            'v_key': v_key,
            'id': id

        }
        items.append(item)

    return items


def movie_details(request, pk):
    m_reviews = get_reviews(pk)
    m_details = movie.details(pk)
    title = m_details.title
    year = m_details.release_date[:4]
    time = m_details.runtime
    desc = m_details.overview
    key = get_video(pk)
    poster = m_details.poster_path
    back = m_details.backdrop_path
    genres = m_details.genres

    details = {'title': title,
               'year': year,
               'time': time,
               'desc': desc,
               'v_key': key,
               'poster': poster,
               'back': back,
               'reviews': m_reviews,
               'genres': genres,
               'id': pk

               }
    return details


def get_reviews(m_id):
    m_reviews = []
    reviews = movie.reviews(m_id)
    for r in reviews:
        review_detail = {
            'author': r.author,
            'content': r.content
        }
        m_reviews.append(review_detail)
    return m_reviews


def get_recommendations(request, pk):
    recs = movie.recommendations(pk)
    r_items = []

    for r in recs:
        title = r.title
        desc = r.overview
        date = r.release_date[:4]
        poster = r.poster_path
        id = r.id
        video = get_video(id)

        r_item = {
            'title': title,
            'desc': desc,
            'year': date,
            'poster': poster,
            'id': id,
            'vkey': video

        }

        r_items.append(r_item)
    return r_items


def get_video(m_id):
    key = ''
    m_details = movie.details(m_id)
    video = m_details.videos.get('results')
    for v in video:
        key = v.get('key')
    return key



