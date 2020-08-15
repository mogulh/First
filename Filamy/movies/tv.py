from tmdbv3api import TMDb, TV

tmdb = TMDb()
tmdb.api_key = 'c903b735b0a2fb0e7df0f76312d6109f'

tv = TV()


def get_tv(request):
    tv_list = []
    tv_shows = tv.popular()
    for t in tv_shows:
        details = tv.details(t.id)
        key = get_tv_video(t.id)

        genres = details.genres
        for g in genres:
            gen = g.get('name')

        title = details.name
        year = details.first_air_date[:4]
        desc = details.overview
        poster = details.poster_path
        back = details.backdrop_path
        v_key = key
        id = t.id
        seasons = details.number_of_seasons
        episode_time = details.episode_run_time[0]

        tv_show = {
            'title': title,
            'year': year,

            'desc': desc,
            'poster': poster,
            'back': back,
            'v_key': v_key,
            'id': id,
            'genres': gen,
            'seasons': seasons,
            'episode_time': episode_time,

        }

        tv_list.append(tv_show)

    return tv_list


def get_tv_video(id):
    key = ''
    tv_details = tv.details(id)
    video = tv_details.videos.get('results')
    for v in video:
        key = v.get('key')
    return key
