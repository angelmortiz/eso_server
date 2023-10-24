from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend

from ..models import Workout
from ..serializers import WorkoutSerializer, WorkoutWithRoutinesSerializer


class WorkoutViewSet(ModelViewSet):
    queryset = Workout.objects.all().select_related('type')
    serializer_class = WorkoutSerializer
    #  Filters
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['target', 'type__name']


class WorkoutWithRoutinesViewSet(WorkoutViewSet):
    queryset = WorkoutViewSet.queryset.prefetch_related('workoutexerciseroutine_set',
                                                        'workoutexerciseroutine_set__exercise',
                                                        'workoutexerciseroutine_set__superset_exercise')
    serializer_class = WorkoutWithRoutinesSerializer
