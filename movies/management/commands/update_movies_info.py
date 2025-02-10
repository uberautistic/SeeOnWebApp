from django.core.management.base import BaseCommand
import requests

from movies.models import Director, Movie

kp2headers = {"X-API-KEY": "000d0977-5dec-43e9-8c92-b142b61e0dfe"}

class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        movies = Movie.objects.all()
        for movie in movies:
            kpid=movie.kpid
            try:
                response = requests.get(
                    url=f'https://kinopoiskapiunofficial.tech/api/v1/staff',
                    headers=kp2headers,
                    params={'filmId':kpid},
                    verify=True
                )
                result = response.json()
            except requests.exceptions.JSONDecodeError as e:
                pass
            for person in result:
                if person['professionKey']=='DIRECTOR':
                    dir_id=person['staffId']
                    try:
                        director = Director.objects.get(kpid=dir_id)
                    except Director.DoesNotExist:
                        director = None
                    if director:
                        movie.director= director
                        movie.save()
                        self.stdout.write(self.style.SUCCESS(f'Фильм {movie.name} обновлен'))
                        if not director.image:
                            director.image=person['posterUrl']
                            director.save()
                            self.stdout.write(self.style.SUCCESS(f'\tРежиссер {director.name} обновлен'))
                    else:
                        new_director= Director(kpid=dir_id,name=person['nameRu'], image=person['posterUrl'])
                        new_director.save()
                        self.stdout.write(self.style.SUCCESS(f'\t\tРежиссер {new_director.name} добавлен'))
                        movie.director = new_director
                        movie.save()
                        self.stdout.write(self.style.SUCCESS(f'Фильм {movie.name} обновлен'))


        self.stdout.write(self.style.SUCCESS('Команда успешно выполнена'))