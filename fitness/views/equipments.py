from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend

from ..models import Equipment
from ..serializers import EquipmentSerializer


class EquipmentViewSet(ModelViewSet):
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer
    # Filters
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['type']
