from rest_framework.filters import SearchFilter
from rest_framework.permissions import DjangoModelPermissions
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend

from ..models import Exercise
from ..pagination import DefaultPagination
from ..serializers import ExerciseSimpleSerializer, ExerciseDetailedSerializer


class ExerciseSimpleViewSet(ModelViewSet):
    queryset = Exercise.objects.all().select_related('main_muscle')
    serializer_class = ExerciseSimpleSerializer

    # Filters
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['difficulty', 'compound_movement', 'main_muscle__name']
    search_fields = ['name', 'alternative_name']

    # Pagination
    pagination_class = DefaultPagination

    # Permissions
    permission_classes = [DjangoModelPermissions]


class ExerciseDetailedViewSet(ExerciseSimpleViewSet):
    queryset = ExerciseSimpleViewSet.queryset.prefetch_related(
        'secondary_muscles', 'types', 'equipments'
    )
    serializer_class = ExerciseDetailedSerializer
