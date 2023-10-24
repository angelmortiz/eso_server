from rest_framework.viewsets import ModelViewSet

from ..models import Exercise
from ..serializers import ExerciseSimpleSerializer, ExerciseDetailedSerializer


class ExerciseSimpleViewSet(ModelViewSet):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSimpleSerializer


class ExerciseDetailedViewSet(ModelViewSet):
    queryset = Exercise.objects.all().select_related('main_muscle').prefetch_related(
        'secondary_muscles', 'types', 'equipments'
    )
    serializer_class = ExerciseDetailedSerializer
