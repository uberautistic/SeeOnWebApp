from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin, UserManager
from django.db import models

from movies.models import Movie


class CustomManager(BaseUserManager):
    def _create_user(self, email, password, first_name, **extra_fields):
        if not email:
            raise ValueError('Email must be provided')
        if not password:
            raise ValueError('Password is not provided')

        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            **extra_fields
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password, first_name, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, first_name, **extra_fields)

    def create_superuser(self, email, password, first_name, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_superuser', True)
        return self._create_user(email, password, first_name, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=100, unique=True, verbose_name='Электронная почта')
    first_name = models.CharField(max_length=240, verbose_name='Имя')
    last_name = models.CharField(max_length=240, verbose_name='Фамилия', blank=True)
    profile_picture = models.ImageField(upload_to='users_pfps/', verbose_name='Фото профиля',
                                        default='users_pfps/user_pfp_placeholder.jpg', blank=True)

    is_calibrated = models.BooleanField(default=False,
                                        verbose_name='Пройдена ли калибровка')
    is_staff = models.BooleanField(default=False,
                                   verbose_name='Сотрудник')  # Поле для обозначения является ли пользователь рабочим
    is_active = models.BooleanField(default=True,
                                    verbose_name='Активный')  # Поле для обозначения является ли аккаунт пользователя активным
    is_superuser = models.BooleanField(default=False,
                                       verbose_name='Суперпользователь')  # Поле для отметки пользователя как суперюзер

    objects = CustomManager()  # Юзер менеджер с методами для создания пользователей и суперюзера, CustomManager() описан выше

    USERNAME_FIELD = 'email'  # Назначение поля имейл как юзернейм
    REQUIRED_FIELDS = ['first_name']  # Необходимые поля для регистрации

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class UserActivityLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    action = models.CharField(max_length=255, verbose_name='Действие')
    timestamp = models.DateTimeField(auto_now_add=True, verbose_name='Таймстемп')
    path = models.CharField(max_length=255, verbose_name='Путь')

    def __str__(self):
        return f'{self.user} - {self.action} at {self.timestamp}'

    class Meta:
        verbose_name = 'Лог пользователя'
        verbose_name_plural = 'Журнал активности'


class Recomendations(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    kpid = models.IntegerField()

    def __str__(self):
        return f'{self.movie.name}-{self.user}'

    class Meta:
        unique_together = ('user', 'movie', 'kpid')

class Watchlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    kpid = models.IntegerField()

    def __str__(self):
        return f'{self.movie.name}-{self.user}'

    class Meta:
        unique_together = ('user', 'movie', 'kpid')
        verbose_name='Избранный фильм'
        verbose_name_plural='Вотчлист'

class Preference(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    movie=models.ForeignKey(Movie,on_delete=models.CASCADE)
    kpid=models.IntegerField()

    def __str__(self):
        return f'{self.movie.name}-{self.user}'

    class Meta:
        unique_together=('user','movie','kpid')
