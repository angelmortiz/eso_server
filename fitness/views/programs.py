from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend

from ..models import Program
from ..serializers import ProgramSerializer, ProgramWithRoutinesSerializer


class ProgramViewSet(ModelViewSet):
    queryset = Program.objects.all().prefetch_related('types')
    serializer_class = ProgramSerializer
    #  Filters
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['sequence', 'duration', 'types__name']


class ProgramWithRoutinesViewSet(ProgramViewSet):
    queryset = ProgramViewSet.queryset.prefetch_related('programworkoutroutine_set',
                                                        'programworkoutroutine_set__workout')
    serializer_class = ProgramWithRoutinesSerializer
