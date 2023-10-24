from rest_framework.viewsets import ModelViewSet

from ..models import Workout
from ..serializers import WorkoutSerializer, WorkoutWithRoutinesSerializer


class WorkoutViewSet(ModelViewSet):
    queryset = Workout.objects.all().select_related('type')
    serializer_class = WorkoutSerializer


class WorkoutWithRoutinesViewSet(ModelViewSet):
    queryset = (Workout.objects.all().select_related('type')
                .prefetch_related('workoutexerciseroutine_set',
                                  'workoutexerciseroutine_set__exercise',
                                  'workoutexerciseroutine_set__superset_exercise'))
    serializer_class = WorkoutWithRoutinesSerializer
