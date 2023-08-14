from django.db import models

from users.models import NULLABLE


class Course(models.Model):
    course_name = models.CharField(max_length=50, unique=True, verbose_name='название курса')
    course_preview = models.ImageField(verbose_name='картинка', **NULLABLE)
    course_description = models.TextField(verbose_name='описание', **NULLABLE)

    class Meta:
        verbose_name = 'курс'
        verbose_name_plural = 'курсы'

    def __str__(self):
        return f'{self.course_name}'
