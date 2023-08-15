from django.contrib import admin

from lessons.models import Lesson


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('lesson_name', 'lesson_description', 'lesson_preview', 'lesson_video_reference', 'course')
