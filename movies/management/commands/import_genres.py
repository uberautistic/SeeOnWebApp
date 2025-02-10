import json
from django.core.management.base import BaseCommand

from movies.models import Genre


class Command(BaseCommand):
    help = 'Загружает фильмы из JSON файла'

    def handle(self, *args, **kwargs):
        with open('json/genres.json', 'r', encoding='utf-8') as genres_file:
            genres = json.load(genres_file)
            for genre_data in genres:
                name = str(genre_data['name']).capitalize()
                slug = genre_data['name']
                new_genre = Genre(name=name, slug=slug)
                new_genre.save()
                self.stdout.write(self.style.SUCCESS(f'Жанр "{new_genre.name}" добавлен в БД'))
        self.stdout.write(self.style.SUCCESS('Команда успешено выполнена'))
