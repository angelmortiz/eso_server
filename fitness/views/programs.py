from rest_framework.viewsets import ModelViewSet

from ..models import Program
from ..serializers import ProgramSerializer, ProgramWithRoutinesSerializer


class ProgramViewSet(ModelViewSet):
    queryset = Program.objects.all().prefetch_related('types')
    serializer_class = ProgramSerializer


class ProgramWithRoutinesViewSet(ModelViewSet):
    queryset = Program.objects.all().prefetch_related('types', 'programworkoutroutine_set',
                                                      'programworkoutroutine_set__workout')
    serializer_class = ProgramWithRoutinesSerializer
