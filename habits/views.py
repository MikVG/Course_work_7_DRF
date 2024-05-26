from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView

from habits.models import Habit
from habits.serializers import HabitSerializer


class HabitCreateAPIView(CreateAPIView):
    """контроллер для создания привычки"""
    serializer_class = HabitSerializer


class HabitListAPIView(ListAPIView):
    """контроллер для отображения списка всех привычек"""
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()


class HabitRetrieveAPIView(RetrieveAPIView):
    """контроллер для отображения конкретной привычки"""
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()


class HabitUpdateAPIView(UpdateAPIView):
    """контроллер для обновления привычки"""
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()


class HabitDestroyAPIView(DestroyAPIView):
    """контроллер для удаления привычки"""
    queryset = Habit.objects.all()


class PublicHabitListAPIView(ListAPIView):
    """контроллер для отображения всех публичных привычек"""
    serializer_class = HabitSerializer
    queryset = Habit.objects.filter(is_public=True)
