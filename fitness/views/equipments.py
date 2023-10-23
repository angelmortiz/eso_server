from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from ..models import Equipment
from ..serializers import EquipmentSerializer


@api_view(['GET'])
def equipment_list(request):
    queryset = Equipment.objects.all()
    serializer = EquipmentSerializer(queryset, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def equipment_detail(request, equipment_id):
    equipment = get_object_or_404(Equipment, id=equipment_id)
    serializer = EquipmentSerializer(equipment)
    return Response(serializer.data)
