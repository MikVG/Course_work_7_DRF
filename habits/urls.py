from django.urls import path
from rest_framework.generics import RetrieveAPIView, UpdateAPIView, DestroyAPIView

from habits.apps import HabitsConfig
from habits.views import HabitCreateAPIView, HabitListAPIView, PublicHabitListAPIView

app_name = HabitsConfig.name


urlpatterns = [
    path('', HabitListAPIView.as_view(), name='habit_list'),
    path('create/', HabitCreateAPIView.as_view(), name='habit_create'),
    path('<int:pk>/', RetrieveAPIView.as_view(), name='habit_detail'),
    path('update/<int:pk>/', UpdateAPIView.as_view(), name='habit_update'),
    path('delete/<int:pk>/', DestroyAPIView.as_view(), name='habit_delete'),
    path('public/', PublicHabitListAPIView.as_view(), name='public_habits'),
]
