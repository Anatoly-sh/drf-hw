from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='почта')
    phone = models.CharField(max_length=35, unique=True, verbose_name='телефон')
    city = models.CharField(max_length=50, verbose_name='город', **NULLABLE)
    avatar = models.ImageField(upload_to='users/', verbose_name='фото', **NULLABLE)
    # first_name = models.CharField(max_length=150, verbose_name='имя', **NULLABLE)
    # last_name = models.CharField(max_length=150, verbose_name='фамилия')
    # is_staff = models.BooleanField(default=False, verbose_name='персонал')
    # is_active = models.BooleanField(default=True, verbose_name='активный статус')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return f'{self.email}'

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'
        # permissions = [
        #
        # ]
