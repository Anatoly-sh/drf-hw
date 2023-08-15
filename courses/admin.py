from django.contrib import admin

from courses.models import Course


@admin.register(Course)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('course_name', 'course_preview', 'course_description')
