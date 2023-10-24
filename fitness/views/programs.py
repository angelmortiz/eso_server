from rest_framework.filters import SearchFilter
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend

from ..models import Program
from ..pagination import DefaultPagination
from ..serializers import ProgramSerializer, ProgramWithRoutinesSerializer


class ProgramViewSet(ModelViewSet):
    queryset = Program.objects.all().prefetch_related('types')
    serializer_class = ProgramSerializer
    # Filters
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['sequence', 'duration', 'types__name']
    search_fields = ['name']
    # Pagination
    pagination_class = DefaultPagination


class ProgramWithRoutinesViewSet(ProgramViewSet):
    queryset = ProgramViewSet.queryset.prefetch_related('programworkoutroutine_set',
                                                        'programworkoutroutine_set__workout')
    serializer_class = ProgramWithRoutinesSerializer
