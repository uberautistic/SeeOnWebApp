
import random
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views import View
from django.views.decorators.http import require_POST

from movies.models import Movie, MoviesGenre, MoviesCountry, Screenshot, Cast, WatchabilityItem, Genre, Country, \
    Director, MediaType
from movies.utils import get_movie_info, get_high_rate_films_for_homepage, \
    get_premieres_list, get_awarded_actors_for_homepage, get_movies_by_name_list, get_similar_list, \
    filter_movies, calculate_recomendations
from users.models import Watchlist, Preference, Recomendations


class CatalogView(View):
    def get(self, request):
        date_sort = request.GET.get('date_sort')
        rating_sort = request.GET.get('rating_sort')
        genres_filter = request.GET.getlist('genres[]')
        countries_filter = request.GET.getlist('countries[]')
        types_filter = request.GET.getlist('types[]')

        director = request.GET.get('director')
        age_rating = request.GET.get('age_rating')

        genres = Genre.objects.all()
        types = MediaType.objects.all()
        countries = Country.objects.all()
        directors = Director.objects.all()

        if request.user.is_authenticated:
            watchlist = Watchlist.objects.filter(user=request.user).values_list('kpid', flat=True)
            if request.user.is_calibrated:
                recomendations_ids = Recomendations.objects.filter(user=request.user).order_by('?').values_list('kpid',
                                                                                                                flat=True)[
                                     :5]
                recomendations = Movie.objects.filter(kpid__in=recomendations_ids)
            else:
                recomendations = []
        else:
            watchlist = []
            recomendations = []
        selectFields = [
            'id', 'name', 'ageRating', 'year', 'poster', 'rating'
        ]
        notNullFields = [
            'id', 'year', 'name', 'rating.imdb', 'poster.url', 'backdrop.url'
        ]
        params = {
            'page': 1,
            'limit': 10,
            'selectFields': selectFields,
            'notNullFields': notNullFields
        }
        if date_sort or rating_sort or genres_filter or countries_filter or director or age_rating or types_filter:
            if not (not date_sort and not rating_sort):
                sortField = []
                sortType = []
                if date_sort:
                    sortField.append('releaseYears.end')
                    sortType.append(str(date_sort))
                if rating_sort:
                    sortField.append('rating.imdb')
                    sortType.append(str(rating_sort))
                params['sortField'] = sortField
                params['sortType'] = sortType
            if genres_filter:
                params['genres.name'] = genres_filter
            if countries_filter:
                params['countries.name'] = countries_filter
            if types_filter:
                params['type'] = types_filter
            else:
                params['type'] = 'movie'
            if director:
                params['persons.id'] = director
                params['persons.profession'] = 'режиссеры'
            if age_rating:
                params['ageRating'] = age_rating
        else:
            genres_list=list(genres.values_list('slug', flat=True))
            genres_filter=random.sample(genres_list,2)

            params['genres.name']=genres_filter
        movies = filter_movies(params)
        context = {
            'genres': genres,
            'types': types,
            'directors': directors,
            'countries': countries,
            'movies': movies,
            'watchlist': watchlist,
            'watchlistids': watchlist,
            'recomendations': recomendations
        }
        return render(request, 'movies/catalog.html', context=context)


class HomePageView(View):
    def get(self, request):
        awarded_actors = get_awarded_actors_for_homepage()
        premieres = get_premieres_list()
        high_rate_movies = get_high_rate_films_for_homepage()
        genres = Genre.objects.filter(is_main=True).order_by('order')
        if request.user.is_authenticated:
            watchlist = Watchlist.objects.filter(user=request.user).values_list('kpid', flat=True)
        else:
            watchlist = []
        if request.user.is_authenticated:
            if request.user.is_calibrated:
                recomendations_ids = Recomendations.objects.filter(user=request.user).order_by('?').values_list('kpid',
                                                                                                                flat=True)[
                                     :5]
                recomendations = Movie.objects.filter(kpid__in=recomendations_ids)
            else:
                recomendations = []
        else:
            recomendations=[]
        context = {
            'movies_high_rating': high_rate_movies,
            'premieres': premieres,
            'actors': awarded_actors,
            'watchlist': watchlist,
            'genres': genres,
            'recomendations': recomendations
        }
        return render(request, 'movies/home.html', context=context)


class CalibrationView(View):
    def get(self, request):
        if request.user.is_calibrated:
            Preference.objects.filter(user=request.user).delete()
            request.user.is_calibrated = False
            request.user.save()
        calibration_movies = Movie.objects.all().order_by('?')[:100]
        if request.user.is_authenticated:
            watchlist = Watchlist.objects.filter(user=request.user).values_list('kpid', flat=True)
        else:
            watchlist = []

        context = {
            'calibration_movies': calibration_movies,
            'watchlist': watchlist
        }
        return render(request, 'movies/calibration.html', context=context)


class FilmPageView(View):
    def get(self, request, pk):
        try:
            movie = Movie.objects.get(kpid=pk)
        except Movie.DoesNotExist:
            movie = None
        if movie:
            film = movie
            countries = MoviesCountry.objects.filter(kpid=pk)
            genres = MoviesGenre.objects.filter(kpid=pk)
            screenshots = Screenshot.objects.filter(kpid=pk)
            cast = Cast.objects.filter(movie_kpid=pk)
            similar_movies = get_similar_list(pk)
            watchability = WatchabilityItem.objects.filter(kpid=pk)
        else:
            film, countries, genres, screenshots, cast, similar_movies, watchability = get_movie_info(pk)
            new_movie = Movie(
                kpid=film.kpid,
                name=film.name, movie_type=film.type, ratingIMDB=film.ratingIMDB,
                ratingKP=film.ratingKP, year=film.year, ageRating=film.ageRating,
                description=film.description, backdropURL=film.backdropURL,
                posterURL=film.posterURL, trailerURL=film.trailerURL
            )
            new_movie.save()
            MoviesCountry.objects.bulk_create([MoviesCountry(kpid=new_movie, country=country) for country in countries])
            MoviesGenre.objects.bulk_create([MoviesGenre(kpid=new_movie, genre=genre) for genre in genres])
            Screenshot.objects.bulk_create([Screenshot(kpid=new_movie, URL=screenshot) for screenshot in screenshots])
            Cast.objects.bulk_create(
                [
                    Cast(movie_kpid=new_movie,
                         kpid=actor.id, name=actor.name,
                         enName=actor.enName, photoURL=actor.photoURL,
                         description=actor.description) for actor in cast
                ]
            )
            WatchabilityItem.objects.bulk_create(
                [
                    WatchabilityItem(kpid=new_movie, name=item.name,
                                     logoURL=item.logoURL, URL=item.URL) for item in watchability
                ]
            )
        if request.user.is_authenticated:
            watchlist = Watchlist.objects.filter(user=request.user).values_list('kpid', flat=True)
        else:
            watchlist = []
        page_context = {'film': film,
                        'countries': countries,
                        'genres': genres,
                        'screenshots': screenshots,
                        'cast': cast,
                        'similar_movies': similar_movies,
                        'watchability': watchability,
                        'watchlist': watchlist
                        }
        return render(request, 'movies/filmpage.html', context=page_context)


@login_required
def toggle_movie_watchlist(request):
    if request.method == 'POST':
        movie_id = request.POST.get('movie_id')
        try:
            movie = Movie.objects.get(kpid=movie_id)
        except Movie.DoesNotExist:
            movie = None
        if not movie:
            film, countries, genres, screenshots, cast, similar_movies, watchability = get_movie_info(movie_id)
            movie = Movie(
                kpid=film.kpid,
                name=film.name, movie_type=film.type, ratingIMDB=film.ratingIMDB,
                ratingKP=film.ratingKP, year=film.year, ageRating=film.ageRating,
                description=film.description, backdropURL=film.backdropURL,
                posterURL=film.posterURL, trailerURL=film.trailerURL
            )
            movie.save()
            MoviesCountry.objects.bulk_create([MoviesCountry(kpid=movie, country=country) for country in countries])
            MoviesGenre.objects.bulk_create([MoviesGenre(kpid=movie, genre=genre) for genre in genres])
            Screenshot.objects.bulk_create([Screenshot(kpid=movie, URL=screenshot) for screenshot in screenshots])
            Cast.objects.bulk_create(
                [
                    Cast(movie_kpid=movie,
                         kpid=actor.id, name=actor.name,
                         enName=actor.enName, photoURL=actor.photoURL,
                         description=actor.description) for actor in cast
                ]
            )
            WatchabilityItem.objects.bulk_create(
                [
                    WatchabilityItem(kpid=movie, name=item.name,
                                     logoURL=item.logoURL, URL=item.URL) for item in watchability
                ]
            )

        film_in_watchlist, created = Watchlist.objects.get_or_create(user=request.user, movie=movie, kpid=movie.kpid)
        calculate_recomendations(request.user)
        if created:
            action = 'added'
        else:
            film_in_watchlist.delete()
            action = 'removed'
        return JsonResponse({'status': 'success', 'action': action})
    return JsonResponse({'status': 'error'}, status=400)


@login_required
@require_POST
def toggle_preferencies(request):
    movie_id = request.POST.get('id')
    movie = Movie.objects.get(kpid=movie_id)
    preference, created = Preference.objects.get_or_create(user=request.user, movie=movie, kpid=movie_id)
    if created:
        status = 'added'
    else:
        status = 'removed'
        preference.delete()
    count = Preference.objects.filter(user=request.user).count()
    response = {
        'status': status,
        'count': count
    }
    return JsonResponse(response)


@login_required
def finish_calibration(request):
    request.user.is_calibrated = True
    request.user.save()
    # рассчет рекомендаций
    calculate_recomendations(request.user)
    return redirect('homepage')


@login_required
def cancel_calibration(request):
    Preference.objects.filter(user=request.user).delete()
    return redirect('homepage')


def search_film_by_name(request):
    if request.GET.get('q'):
        q = request.GET.get('q')
        search_result = get_movies_by_name_list(q)
        context = {
            'search_result': search_result
        }
        return render(request, 'movies/search_result.html', context)
    else:
        return None


def search_country(request):
    q = request.GET.get('q', '')
    countries = Country.objects.filter(name__iregex=q)
    context = {'countries': countries}
    return render(request, 'movies/search-countries.html', context=context)


def search_directors(request):
    q_dir = request.GET.get('q_dir', '')
    directors = Director.objects.filter(name__iregex=q_dir)
    context = {'directors': directors}
    return render(request, 'movies/search-directors.html', context=context)


def search_genres(request):
    q_genre = request.GET.get('q_genre', '')
    genres = Genre.objects.filter(name__iregex=q_genre)
    context = {'genres': genres}
    return render(request, 'movies/search-genres.html', context=context)


def filter(request):
    date_sort = request.GET.get('date_sort')
    rating_sort = request.GET.get('rating_sort')
    genres_filter = request.GET.getlist('genres[]')
    countries_filter = request.GET.getlist('countries[]')
    types_filter = request.GET.getlist('types[]')
    director = request.GET.get('director')
    age_rating = request.GET.get('age_rating')

    selectFields = [
        'id', 'name', 'ageRating', 'year', 'poster', 'rating'
    ]
    notNullFields = [
        'id', 'year', 'name', 'rating.imdb', 'poster.url', 'backdrop.url'
    ]
    params = {
        'page': 1,
        'limit': 10,
        'selectFields': selectFields,
        'notNullFields': notNullFields
    }
    if request.user.is_authenticated:
        watchlist = Watchlist.objects.filter(user=request.user).values_list('kpid', flat=True)

    else:
        watchlist = []
    if date_sort or rating_sort or genres_filter or countries_filter or director or age_rating or types_filter:
        if not (not date_sort and not rating_sort):
            sortField = []
            sortType = []
            if date_sort:
                sortField.append('releaseYears.end')
                sortType.append(str(date_sort))
            if rating_sort:
                sortField.append('rating.imdb')
                sortType.append(str(rating_sort))
            params['sortField'] = sortField
            params['sortType'] = sortType
        if genres_filter:
            params['genres.name'] = genres_filter
        if countries_filter:
            params['countries.name'] = countries_filter
        if types_filter:
            params['type'] = types_filter
        else:
            params['type'] = 'movie'
        if director:
            params['persons.id'] = director
            params['persons.profession'] = 'режиссеры'
        if age_rating:
            params['ageRating'] = age_rating

    movies = filter_movies(params)
    context = {
        'watchlist': watchlist,
        'watchlistids': watchlist,
        'movies': movies,
    }
    return render(request, 'movies/filter_result.html', context=context)


def refresh_recommendations(request):
    if request.user.is_authenticated:
        watchlist = Watchlist.objects.filter(user=request.user).values_list('kpid', flat=True)
        if request.user.is_calibrated:
            recomendations_ids = Recomendations.objects.filter(user=request.user).order_by('?').values_list('kpid',
                                                                                                            flat=True)[
                                 :5]
            recomendations = Movie.objects.filter(kpid__in=recomendations_ids)
        else:
            recomendations = []
    else:
        watchlist = []
        recomendations = []
    context = {
        'recomendations': recomendations,
        'watchlist': watchlist,
        'watchlistids': watchlist
    }
    return render(request, 'movies/recomendations_result.html', context=context)
