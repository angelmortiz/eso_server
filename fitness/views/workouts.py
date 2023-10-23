from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from ..models import Workout
from ..serializers import WorkoutSerializer


@api_view(['GET'])
def workout_list(request):
    queryset = Workout.objects.all()
    serializer = WorkoutSerializer(queryset, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def workout_detail(request, workout_id):
    workout = get_object_or_404(Workout, id=workout_id)
    serializer = WorkoutSerializer(workout)
    return Response(serializer.data)
