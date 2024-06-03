from rest_framework.serializers import ValidationError


class RelatedHabitValidators:
    """Валидатор для исключения одновременного выбора связанной привычки и указания вознаграждения"""
    def __init__(self, related_habit, award):
        self.related_habit = related_habit
        self.award = award

    def __call__(self, value):
        related_habit = dict(value).get(self.related_habit)
        award = dict(value).get(self.award)
        if related_habit and award:
            raise ValidationError("Нельзя одновременно выбрать связанную привычку и вознаграждение")


class LeadTimeValidator:
    """Валидатор для проверки, что время выполнения не больше 120 секунд"""
    def __init__(self, lead_time):
        self.lead_time = lead_time

    def __call__(self, value):
        lead_time = dict(value).get(self.lead_time)
        if int(lead_time) > 120:
            raise ValidationError("Время выполнения должно быть не больше 120 секунд")


class RelatedGoodHabitValidator:
    """Валидатор для проверки, что в связанные привычки могут попадать только привычки с признаком приятной привычки"""
    def __init__(self, related_habit, good_habit):
        self.related_habit = related_habit
        self.good_habit = good_habit

    def __call__(self, value):
        related_habit = dict(value).get(self.related_habit)
        good_habit = dict(value).get(self.good_habit)
        if related_habit and not related_habit.good_habit:
            raise ValidationError("В связанные привычки могут попадать только привычки с признаком приятной привычки")


class GoodHabitNotAwardAndRelatedHabitValidator:
    """Валидатор для проверки, что у приятной привычки не может быть вознаграждения или связанной привычки"""
    def __init__(self, good_habit, award, related_habit):
        self.good_habit = good_habit
        self.award = award
        self.related_habit = related_habit

    def __call__(self, value):
        good_habit = dict(value).get(self.good_habit)
        award = dict(value).get(self.award)
        related_habit = dict(value).get(self.related_habit)
        if good_habit and (award or related_habit):
            raise ValidationError("У приятной привычки не может быть вознаграждения или связанной привычки")


class RepeatValidator:
    """Валидатор, который проверяет, что нельзя выполнять привычку реже, чем 1 раз в 7 дней. Хотя для моей модели
    эта проверка не актуальна, но вне проверку, что период выполнения не соответствует данным из поля выбора
    заложенные в модели"""
    def __init__(self, period):
        self.period = period

    def __call__(self, value):
        period = dict(value).get(self.period)
        if period not in ['daily', 'two_days', 'weekly']:
            raise ValidationError('нельзя выполнять привычку реже, чем 1 раз в 7 дней')
