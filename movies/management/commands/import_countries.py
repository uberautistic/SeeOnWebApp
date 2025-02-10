import json
from django.core.management.base import BaseCommand

from movies.models import Country


class Command(BaseCommand):
    help = 'Загружает фильмы из JSON файла'

    def handle(self, *args, **kwargs):
        with open('json/countries.json', 'r', encoding='utf-8') as countries_file:
            countries = json.load(countries_file)
            for country_data in countries:
                name = country_data['name']
                slug = country_data['slug']
                new_country = Country(name=name, slug=slug)
                new_country.save()
                self.stdout.write(self.style.SUCCESS(f'Страна "{new_country.name}" добавленa в БД'))
        self.stdout.write(self.style.SUCCESS('Команда успешено выполнена'))
