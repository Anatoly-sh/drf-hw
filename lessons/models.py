from django.db import models

from courses.models import Course
from users.models import NULLABLE


class Lesson(models.Model):
    lesson_name = models.CharField(max_length=150, verbose_name='название урока')
    lesson_description = models.TextField(verbose_name='описание урока')
    lesson_preview = models.ImageField(verbose_name='картинка', **NULLABLE)
    lesson_video_reference = models.URLField(verbose_name="ссылка на видео", **NULLABLE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='курс', **NULLABLE)

    class Meta:
        verbose_name = 'урок'
        verbose_name_plural = 'уроки'

    def __str__(self):
        return f'{self.lesson_name}'
