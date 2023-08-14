from django.urls import path

from lessons.views import *

urlpatterns = [
    path('', LessonListView.as_view(), name='lessons-list'),
    path('detail/<int:pk>/', LessonDetailView.as_view(), name='lessons-detail'),
    path('create/', LessonCreateView.as_view(), name='lessons-create'),
    path('update/<int:pk>/', LessonUpdateView.as_view(), name='lessons-update'),
    path('delete/', LessonDeleteView.as_view(), name='lessons-delete'),
]
