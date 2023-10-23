from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from ..models import Muscle
from ..serializers import MuscleSerializer


@api_view(['GET'])
def muscle_list(request):
    queryset = Muscle.objects.all()
    serializer = MuscleSerializer(queryset, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def muscle_detail(request, muscle_id):
    muscle = get_object_or_404(Muscle, id=muscle_id)
    serializer = MuscleSerializer(muscle)
    return Response(serializer.data)
