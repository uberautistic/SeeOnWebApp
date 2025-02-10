import json
from django.core.management.base import BaseCommand

from movies.models import Movie, WatchabilityItem, Screenshot, Cast, MoviesGenre, MoviesCountry
from movies.utils import get_movie_info


class Command(BaseCommand):
    help = 'Загружает фильмы из JSON файла'

    def handle(self, *args, **kwargs):
        with open('json/top100movies.json', 'r', encoding='utf-8') as movie_file:
            movies = json.load(movie_file)['docs']
            for movie_data in movies:
                kpid = movie_data['id']
                try:
                    movie = Movie.objects.get(kpid=kpid)
                except Movie.DoesNotExist:
                    movie = None
                if not movie:
                    film, countries, genres, screenshots, cast, similar_movies, watchability = get_movie_info(kpid)
                    movie = Movie(
                        kpid=film.kpid,
                        name=film.name, movie_type=film.type, ratingIMDB=film.ratingIMDB,
                        ratingKP=film.ratingKP, year=film.year, ageRating=film.ageRating,
                        description=film.description, backdropURL=film.backdropURL,
                        posterURL=film.posterURL, trailerURL=film.trailerURL
                    )
                    movie.save()
                    MoviesCountry.objects.bulk_create(
                        [MoviesCountry(kpid=movie, country=country) for country in countries])
                    MoviesGenre.objects.bulk_create([MoviesGenre(kpid=movie, genre=genre) for genre in genres])
                    Screenshot.objects.bulk_create(
                        [Screenshot(kpid=movie, URL=screenshot) for screenshot in screenshots])
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
                    self.stdout.write(self.style.SUCCESS(
                        f'Фильм "{movie.name}" добавлен в БД, KPID:{movie.kpid}'))  # Выводим сообщение об успешном создании
            self.stdout.write(self.style.SUCCESS('Команда успешено выполнена'))
