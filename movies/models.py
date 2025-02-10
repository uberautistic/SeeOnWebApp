from django.db import models


class Director(models.Model):
    kpid = models.IntegerField(verbose_name='ID режиссера на КП', unique=True)
    image = models.ImageField(verbose_name='Фото', null=True)
    name = models.CharField(verbose_name='Имя Фамилия', max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Режиссер'
        verbose_name_plural = 'Режиссеры'

class Movie(models.Model):
    kpid = models.IntegerField(verbose_name='ID Кинопоиск', unique=True)
    name = models.CharField(max_length=255, verbose_name='Название', blank=True)
    movie_type = models.CharField(verbose_name='Тип', max_length=255, default=True)
    ratingIMDB = models.FloatField(blank=True, verbose_name='Рейтинг IMDB')
    ratingKP = models.FloatField(blank=True, verbose_name='Рейтинг Кинопоиск')
    year = models.CharField(max_length=4, blank=True, verbose_name='Год выпуска')
    ageRating = models.CharField(max_length=3, blank=True, verbose_name='Возрастной рейтинг')
    description = models.TextField(blank=True, verbose_name='Описание')

    director = models.ForeignKey(Director,on_delete=models.CASCADE, null=True)

    backdropURL = models.URLField(blank=True, verbose_name='Фон')
    posterURL = models.URLField(blank=True, verbose_name='Постер')
    trailerURL = models.URLField(blank=True, verbose_name='Ссылка на трейлер')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'


class WatchabilityItem(models.Model):
    kpid = models.ForeignKey(Movie, to_field='kpid', on_delete=models.CASCADE)
    name = models.CharField(max_length=255, verbose_name='Название сервиса', blank=True)
    logoURL = models.URLField(blank=True, verbose_name='Лого сервиса')
    URL = models.URLField(blank=True, verbose_name='Ссылка')

    def __str__(self):
        return self.URL

    class Meta:
        verbose_name = 'Ссылка на сервис'
        verbose_name_plural = 'Ссылки на сервисы'


class Screenshot(models.Model):
    kpid = models.ForeignKey(Movie, to_field='kpid', on_delete=models.CASCADE, blank=True)
    URL = models.URLField(blank=True, verbose_name='Ссылка')

    def __str__(self):
        return self.URL

    class Meta:
        verbose_name = 'Скриншот'
        verbose_name_plural = 'Скриншоты'


class Genre(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')
    order = models.IntegerField(default=0)
    slug = models.CharField(max_length=255)
    is_main = models.BooleanField(default=False)
    picture = models.ImageField(null=True, verbose_name='Изображение', upload_to='movies/genres/pictures', )
    icon = models.ImageField(null=True, verbose_name='Иконка', upload_to='movies/genres/icons')
    subtitle = models.CharField(max_length=255, verbose_name='Подпись в карточке', default=' ', null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'


class MoviesGenre(models.Model):
    kpid = models.ForeignKey(Movie, to_field='kpid', on_delete=models.CASCADE, verbose_name='ID фильма на кинопоиске')
    genre = models.CharField(max_length=255, verbose_name='Жанр')

    def __str__(self):
        return self.genre

    class Meta:
        verbose_name = 'Жанр фильма'
        verbose_name_plural = 'Жанры фильма'


class Country(models.Model):
    name = models.CharField(max_length=255)
    slug = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Страна'
        verbose_name_plural = 'Страны'


class MoviesCountry(models.Model):
    kpid = models.ForeignKey(Movie, to_field='kpid', on_delete=models.CASCADE, verbose_name='ID на кинопоиске')
    country = models.CharField(max_length=255, verbose_name='Страна производства')

    def __str__(self):
        return self.country

    class Meta:
        verbose_name = 'Страна производства фильма'
        verbose_name_plural = 'Страны производства фильмов'





class MediaType(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')
    slug = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тип контента'
        verbose_name_plural = 'Типы контента'


class Cast(models.Model):
    movie_kpid = models.ForeignKey(Movie, to_field='kpid', on_delete=models.CASCADE,
                                   verbose_name='ID фильма на кинопоиске')
    kpid = models.IntegerField()
    name = models.CharField(max_length=255, verbose_name='Имя')
    enName = models.CharField(max_length=255, verbose_name='Имя на англ.')
    photoURL = models.URLField(verbose_name='Ссылка на фото')
    description = models.CharField(max_length=255, verbose_name='Описание', blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Актер фильма'
        verbose_name_plural = 'Актеры фильмов'
