from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend

from ..models import Muscle
from ..serializers import MuscleSerializer


class MuscleViewSet(ModelViewSet):
    queryset = Muscle.objects.all()
    serializer_class = MuscleSerializer
    # Filters
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['type']
