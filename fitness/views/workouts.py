from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from ..models import Workout
from ..serializers import WorkoutSerializer, WorkoutWithRoutinesSerializer


@api_view(['GET'])
def workout_list_simple(request):
    queryset = Workout.objects.all()
    serializer = WorkoutSerializer(queryset, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def workout_list_with_routines(request):
    queryset = Workout.objects.all().prefetch_related('workoutexerciseroutine_set',
                                                      'workoutexerciseroutine_set__exercise',
                                                      'workoutexerciseroutine_set__superset_exercise')
    serializer = WorkoutWithRoutinesSerializer(queryset, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def workout_detail(request, workout_id):
    workout = get_object_or_404(Workout, id=workout_id)
    serializer = WorkoutSerializer(workout)
    return Response(serializer.data)


@api_view(['GET'])
def workout_detail_with_routines(request, workout_id):
    try:
        workout = Workout.objects.prefetch_related(
            'workoutexerciseroutine_set__exercise',
            'workoutexerciseroutine_set__superset_exercise'
        ).get(id=workout_id)
    except Workout.DoesNotExist:
        return Response({'error': 'Workout not found'}, status=status.HTTP_404_NOT_FOUND)

    serializer = WorkoutWithRoutinesSerializer(workout)
    return Response(serializer.data)
