from django.core.management.base import BaseCommand
import requests

from movies.models import Director, Movie

kp2headers = {"X-API-KEY": "000d0977-5dec-43e9-8c92-b142b61e0dfe"}

class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        directors = Director.objects.all()

        for director in directors:
            if not director.image:
                dir_id=director.kpid
                try:
                    response = requests.get(
                        url=f'https://kinopoiskapiunofficial.tech/api/v1/staff/{dir_id}',
                        headers=kp2headers,
                        verify=True
                    )
                    result = response.json()
                    director.image=result['posterUrl']
                    director.save()
                    self.stdout.write(self.style.SUCCESS(f'Режиссер {director.name} обновлен'))
                except requests.exceptions.JSONDecodeError as e:
                    pass

        self.stdout.write(self.style.SUCCESS('Команда успешно выполнена'))