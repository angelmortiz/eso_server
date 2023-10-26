from rest_framework.filters import SearchFilter
from rest_framework.permissions import DjangoModelPermissions
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend

from ..models import Workout
from ..pagination import DefaultPagination
from ..serializers import WorkoutSerializer, WorkoutWithRoutinesSerializer


class WorkoutViewSet(ModelViewSet):
    queryset = Workout.objects.all().select_related('type')
    serializer_class = WorkoutSerializer

    #  Filters
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['target', 'type__name']
    search_fields = ['name', 'variant']

    # Pagination
    pagination_class = DefaultPagination

    # Permissions
    permission_classes = [DjangoModelPermissions]


class WorkoutWithRoutinesViewSet(WorkoutViewSet):
    queryset = WorkoutViewSet.queryset.prefetch_related('workoutexerciseroutine_set',
                                                        'workoutexerciseroutine_set__exercise',
                                                        'workoutexerciseroutine_set__superset_exercise')
    serializer_class = WorkoutWithRoutinesSerializer
