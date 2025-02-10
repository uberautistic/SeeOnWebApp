from django.contrib import admin

from movies.models import Movie, Genre, Director, Country, MediaType

admin.site.register(Movie)
admin.site.register(Genre)
admin.site.register(Director)
admin.site.register(Country)
admin.site.register(MediaType)
