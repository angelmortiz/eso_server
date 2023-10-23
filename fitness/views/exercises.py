from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from ..models import Exercise
from ..serializers import ExerciseSimpleSerializer, ExerciseDetailSerializer


@api_view(['GET'])
def exercise_list_simple(request):
    queryset = Exercise.objects.all()
    serializer = ExerciseSimpleSerializer(queryset, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def exercise_list_detail(request):
    queryset = Exercise.objects.all().select_related('main_muscle').prefetch_related(
        'secondary_muscles', 'types', 'equipments'
    )
    serializer = ExerciseDetailSerializer(queryset, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def exercise_detail(request, exercise_id):
    exercise = get_object_or_404(Exercise, id=exercise_id)
    serializer = ExerciseDetailSerializer(exercise)
    return Response(serializer.data)
