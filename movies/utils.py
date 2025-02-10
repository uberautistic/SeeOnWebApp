import datetime
from collections import Counter
from itertools import chain

import requests
import logging

from movies.dataclasses import MoviePreviewDataClass, PersonPreviewDataClass, MovieDetailDataClass, WatchabilityItem
from movies.models import Movie, MoviesGenre, MoviesCountry
from users.models import Preference, Watchlist, Recomendations

kp1headers = {"X-API-KEY": "токенДляАпиКинопоиска"}
kp2headers = {"X-API-KEY": "токенДляВторогоАпи"}

"""
                ЗАПРОСЫ К АПИШКАМ
"""


def get_high_rate_movies(limit=10):
    try:
        selectFields = ['id', 'name', 'enName', 'rating', 'ageRating', 'poster', 'year', 'type']
        notNullFields = ['id', 'name', 'poster.url']
        params = {
            'limit': limit,
            'selectField': selectFields,
            'notNullFields': notNullFields,
            'sortField': 'rating.imdb',
            'sortType': '-1',
            'lists': 'top250'
        }
        response = requests.get(
            url='https://api.kinopoisk.dev/v1.4/movie',
            headers=kp1headers,
            params=params,

            verify=True
        )
        return response.json()['docs']
    except requests.exceptions.JSONDecodeError as e:
        logging.error(f'Ошибка в получении фильмов с высоким рейтом, {e}')
    return None


def get_movies_by_name(name):
    try:
        params = {
            'page': 1,
            'limit': 10,
            'query': name
        }
        response = requests.get(
            url='https://api.kinopoisk.dev/v1.4/movie/search',
            headers=kp1headers,
            params=params,

            verify=True
        )
        return response.json()['docs']
    except requests.exceptions.JSONDecodeError as e:
        logging.error(f'Ошибка в получении фильмов по названию, {e}')
    return None


def get_movies_by_genre(genre):
    try:
        notNullFields = [
            'id', 'year', 'rating.imdb', 'poster.url', 'backdrop.url'
        ]
        params = {
            'page': 1,
            'limit': 10,
            'genres.name': genre,
            'notNullFields': notNullFields
        }
        response = requests.get(
            url='https://api.kinopoisk.dev/v1.4/movie',
            headers=kp1headers,
            params=params,

            verify=True
        )
        return response.json()['docs']
    except requests.exceptions.JSONDecodeError as e:
        logging.error(f'Ошибка в получении фильмов по названию, {e}')
    return None


def get_trailer(pk):
    try:
        response = requests.get(
            url=f'https://kinopoiskapiunofficial.tech/api/v2.2/films/{pk}/videos',
            headers=kp2headers,

            verify=True
        )
        result = response.json()
        return result['items'][0]['url'] if result['total'] != 0 else ''
    except requests.exceptions.JSONDecodeError as e:
        logging.error(f'Ошибка в получении трейлера, {e}')
    return None


def get_premieres():
    try:
        year = datetime.datetime.now().year
        month = datetime.datetime.now().strftime('%B').upper()
        params = {
            'year': year,
            'month': month
        }
        response = requests.get(
            url='https://kinopoiskapiunofficial.tech/api/v2.2/films/premieres',
            headers=kp2headers,
            params=params,

            verify=True
        )
        return response.json()['items']
    except requests.exceptions.JSONDecodeError as e:
        logging.error(f'Ошибка в получении премьер, {e}')
    return None


def get_movies_by_filter(params):
    try:

        response = requests.get(
            url='https://api.kinopoisk.dev/v1.4/movie',
            headers=kp1headers,
            params=params,

            verify=True
        )

        return response.json()['docs']
    except requests.exceptions.JSONDecodeError as e:

        logging.error(f'Ошибка в получении фильмов по названию, {e}')
    return None


def get_awarded_actors(limit=10):
    try:
        selectFields = ['id', 'name', 'enName', 'photo']
        notNullFields = ['name', 'photo']
        params = {
            'limit': limit,
            'selectFields': selectFields,
            'notNullFields': notNullFields,
            'sortField': 'countAwards',
            'sortType': '-1',
            'profession.value': 'Актер'
        }
        response = requests.get(
            url='https://api.kinopoisk.dev/v1.4/person',
            headers=kp1headers,
            params=params,

            verify=True
        )
        return response.json()['docs']
    except requests.exceptions.JSONDecodeError as e:
        logging.error(f'Ошибка в получении актеров с наградами, {e}')
    return None


def get_movie_info_json(pk):
    try:
        response = requests.get(
            url=f'https://api.kinopoisk.dev/v1.4/movie/{pk}',
            headers=kp1headers,

            verify=True
        )
        return response.json()
    except requests.exceptions.JSONDecodeError as e:
        logging.error(f'Ошибка в получении фильма, {e}')
    return None


def get_screenshots(pk):
    try:
        params = {
            'type': 'SCREENSHOT',
            'page': 1
        }
        response = requests.get(
            url=f'https://kinopoiskapiunofficial.tech/api/v2.2/films/{pk}/images',
            params=params,
            headers=kp2headers,

            verify=True
        )
        return response.json()['items']
    except requests.exceptions.JSONDecodeError as e:
        logging.error(f'Ошибка в получении скриншотов, {e}')
    return None


def get_frames(pk):
    try:
        params = {
            'page': 1,
            'limit': 10,
            'selectFields': 'url',
            'notNullFields': 'url',
            'movieId': pk,
            'type': 'screenshot'
        }
        response = requests.get(
            url='https://api.kinopoisk.dev/v1.4/image',
            params=params,
            headers=kp1headers,

            verify=True
        )
        return response.json()['docs']
    except requests.exceptions.JSONDecodeError as e:
        logging.error(f'Ошибка в получении кадров, {e}')
    return None


def get_similar_movies(pk):
    try:
        response = requests.get(
            url=f'https://kinopoiskapiunofficial.tech/api/v2.2/films/{pk}/similars',
            headers=kp2headers,

            verify=True
        )
        return response.json()['items']
    except requests.exceptions.JSONDecodeError as e:
        logging.error(f'Ошибка в получении похожих, {e}')
    return None


"""
                ОБРАБОТКА JSON
"""


def get_high_rate_films_for_homepage():
    movies_list_json = get_high_rate_movies(limit=5)
    movies_list = []
    for movie in movies_list_json:
        kpid = movie['id']
        name = movie['name']
        year = movie['year']
        ageRating = movie['ageRating']
        posterURL = movie['poster']['url']
        ratingIMDB = movie['rating']['imdb']
        movies_list.append(
            MoviePreviewDataClass(
                id=kpid, name=name, year=year,
                ageRating=ageRating, posterURL=posterURL,
                ratingIMDB=ratingIMDB
            )
        )
    return movies_list


def get_premieres_list():
    movies_list_json = get_premieres()
    movies_list = []
    for movie in movies_list_json:
        kpid = movie['kinopoiskId']
        name = movie['nameRu']
        year = movie['year']
        date = datetime.datetime.strptime(movie['premiereRu'], '%Y-%m-%d')
        posterURL = movie['posterUrlPreview']
        if date >= date.today():
            movies_list.append(
                MoviePreviewDataClass(
                    id=kpid, name=name, year=year,
                    posterURL=posterURL, premiereDate=transform_date(movie['premiereRu'])
                )
            )
    return movies_list[:3]


def get_awarded_actors_for_homepage():
    actors_json = get_awarded_actors(5)
    actors = []
    for actor in actors_json:
        kpid = actor['id']
        name = actor['name']
        enName = actor['enName']
        photoURL = actor['photo']
        actors.append(
            PersonPreviewDataClass(
                id=kpid, name=name,
                enName=enName, photoURL=photoURL
            )
        )
    return actors

# получение информации о фильме
def get_movie_info(pk):
    movie = get_movie_info_json(pk)

    kpid = movie['id']
    name = movie['name']
    movie_type = movie['type']
    ratingIMDB = movie['rating']['imdb']
    ratingKP = movie['rating']['kp']
    year = movie['year']
    ageRating = str(movie['ageRating']) + '+'
    description = movie['description']
    backdropURL = movie['backdrop']['url'] if movie['backdrop']['url'] \
        else 'https://avatars.mds.yandex.net/i?id=1ac9c8b0c3f7570c7709d8190aa8c4e4_l-5209520-images-thumbs&n=13'
    posterURL = movie['poster']['url'] if movie['poster']['url'] \
        else 'https://newsrnd.com/images/no-image.png'
    trailerURL = get_trailer(pk)
    watchability = []
    if movie.get('watchability') != None:
        if movie['watchability']['items']:
            for item in movie['watchability']['items']:
                watchability.append(
                    WatchabilityItem(
                        name=item['name'],
                        logoURL=item['logo']['url'],
                        URL=item['url']
                    )
                )
    countries = [country['name'] for country in movie['countries']]
    genres = [genre['name'] for genre in movie['genres']]
    cast = []
    for person in movie['persons']:
        if person['enProfession'] == 'actor':
            cast.append(
                PersonPreviewDataClass(
                    id=person['id'],
                    name=person['name'] if person['name'] else '',
                    enName=person['enName'] if person['enName'] else '',
                    description=person['description'] if person['description'] else '',
                    photoURL=person['photo']
                )
            )
    screenshots_json = get_frames(pk)
    screenshots = [screenshot['url'] for screenshot in screenshots_json]
    similar_movies = get_similar_list(pk)
    return MovieDetailDataClass(
        kpid=kpid, name=name, type=movie_type,
        description=description, year=year,
        ratingIMDB=ratingIMDB, ratingKP=ratingKP,
        ageRating=ageRating, posterURL=posterURL, backdropURL=backdropURL,
        trailerURL=trailerURL
    ), countries, genres, screenshots, cast, similar_movies, watchability

# поиск по названию
def get_movies_by_name_list(name):
    movies_list_json = get_movies_by_name(name)
    movies_list = []
    for movie in movies_list_json[:5]:
        kpid = movie['id']
        name = movie['name']
        year = movie['year']
        ageRating = movie['ageRating']
        posterURL = movie['poster']['url'] if movie['poster']['url'] else 'https://newsrnd.com/images/no-image.png'
        ratingIMDB = movie['rating']['imdb']
        movies_list.append(
            MoviePreviewDataClass(
                id=kpid, name=name, year=year,
                ageRating=ageRating, posterURL=posterURL,
                ratingIMDB=ratingIMDB
            )
        )
    return movies_list


def transform_date(date):
    months = ['января', 'февраля', 'марта', 'апреля', 'мая', 'июня',
              'июля', 'августа', 'сентября', 'октября', 'ноября', 'декабря']
    year, month, day = date.split('-')
    return f'{day.lstrip("0")} {months[int(month) - 1]}'

# фильтрация
def filter_movies(params):
    movies_json = get_movies_by_filter(params)

    movies = []
    for movie_json in movies_json:
        id = movie_json['id']
        name = movie_json['name']
        year = movie_json['year']
        posterURL = movie_json['poster']['url']
        ratingIMDB = movie_json['rating']['imdb']
        ageRating = movie_json['ageRating']
        movies.append(MoviePreviewDataClass(
            id=id, name=name, year=year,
            ageRating=ageRating, posterURL=posterURL,
            ratingIMDB=ratingIMDB
        ))

    return movies


def get_similar_list(pk):
    similar_movies = []
    similar_movies_json = get_similar_movies(pk)
    for similar_movie in similar_movies_json:
        similar_movies.append(
            MoviePreviewDataClass(
                id=similar_movie['filmId'],
                name=similar_movie['nameRu'],
                posterURL=similar_movie['posterUrl']
            )
        )
    return similar_movies


def get_movies_by_genre_list(genre):
    movies = []
    movies_json = get_movies_by_genre(genre)
    for movie in movies_json:
        kpid = movie['id']
        name = movie['name'][:16]
        year = movie['year']
        ageRating = movie['ageRating']
        if 'poster' in movie:
            posterURL = movie['poster']['url'] if movie['poster']['url'] else 'https://newsrnd.com/images/no-image.png'
        else:
            posterURL = 'https://newsrnd.com/images/no-image.png'
        ratingIMDB = movie['rating']['imdb']
        movies.append(
            MoviePreviewDataClass(
                id=kpid, name=name, year=year,
                ageRating=ageRating, posterURL=posterURL,
                ratingIMDB=ratingIMDB
            )
        )
    return movies

# расчет рекомендаций
def calculate_recomendations(user):
    Recomendations.objects.filter(user=user).delete()
    preferences = Preference.objects.filter(user=user)
    watchlist = Watchlist.objects.filter(user=user)
    interesting_movies_ids = preferences.values_list('kpid', flat=True).union(watchlist.values_list('kpid', flat=True))
    interesting_movies_ids_wo_duplicates = list(set(interesting_movies_ids))
    interesting_movies = Movie.objects.filter(kpid__in=interesting_movies_ids_wo_duplicates)
    genres = []
    directors = []
    for movie in interesting_movies:
        movie_genres = MoviesGenre.objects.filter(kpid=movie.kpid).values_list('genre', flat=True)
        if movie.director:
            director = movie.director.kpid
            directors.append(director)
        genres = genres + list(movie_genres)

    g_counter = Counter(genres)
    d_counter = Counter(directors)

    most_common_genres = g_counter.most_common(3)
    most_common_directors = d_counter.most_common(4)

    genre_preferences = [genre for genre, count in most_common_genres]
    director_preferences = [director for director, count in most_common_directors]
    movies = Movie.objects.exclude(kpid__in=preferences.values_list('kpid', flat=True))
    for movie in movies:
        movie_genres = MoviesGenre.objects.filter(kpid=movie.kpid).values_list('genre', flat=True)
        if movie.director:
            director = movie.director.kpid
            if set(movie_genres).issubset(genre_preferences) or director in director_preferences:
                new_rec = Recomendations(user=user, movie=movie, kpid=movie.kpid)
                new_rec.save()
        else:
            if set(movie_genres).issubset(genre_preferences):
                new_rec = Recomendations(user=user, movie=movie, kpid=movie.kpid)
                new_rec.save()

    return Recomendations.objects.filter(user=user)
