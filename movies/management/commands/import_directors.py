import json
from django.core.management.base import BaseCommand

from movies.models import Director





class Command(BaseCommand):
    help = 'Загружает фильмы из JSON файла'

    def handle(self, *args, **kwargs):
        with open('json/directors.json', 'r', encoding='utf-8') as directors_file:
            directors = json.load(directors_file)
            for director_data in directors:
                name=director_data['name']
                kpid=director_data['id']
                new_director=Director(name=name, kpid=kpid)
                new_director.save()
                self.stdout.write(self.style.SUCCESS(f'Режиссер "{new_director.name}" добавлен в БД'))
        self.stdout.write(self.style.SUCCESS('Команда успешено выполнена'))
