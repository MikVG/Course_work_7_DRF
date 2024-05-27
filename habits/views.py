from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView

from habits.models import Habit
from habits.paginators import HabitPaginator
from habits.serializers import HabitSerializer
from users.permissions import IsOwner


class HabitCreateAPIView(CreateAPIView):
    """контроллер для создания привычки"""
    serializer_class = HabitSerializer

    def perform_create(self, serializer):
        habit = serializer.save()
        habit.user = self.request.user
        habit.save()


class HabitListAPIView(ListAPIView):
    """контроллер для отображения списка всех привычек"""
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    pagination_class = HabitPaginator
    permission_classes = (IsOwner,)


class HabitRetrieveAPIView(RetrieveAPIView):
    """контроллер для отображения конкретной привычки"""
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    # permission_classes = (IsOwner,)


class HabitUpdateAPIView(UpdateAPIView):
    """контроллер для обновления привычки"""
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = (IsOwner,)


class HabitDestroyAPIView(DestroyAPIView):
    """контроллер для удаления привычки"""
    queryset = Habit.objects.all()
    permission_classes = (IsOwner,)


class PublicHabitListAPIView(ListAPIView):
    """контроллер для отображения всех публичных привычек"""
    serializer_class = HabitSerializer
    queryset = Habit.objects.filter(is_public=True)
