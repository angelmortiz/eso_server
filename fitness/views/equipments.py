from rest_framework.viewsets import ModelViewSet

from ..models import Equipment
from ..serializers import EquipmentSerializer


class EquipmentViewSet(ModelViewSet):
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer
