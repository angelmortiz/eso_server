from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from ..models import Program
from ..serializers import ProgramSerializer, ProgramWithRoutinesSerializer


@api_view(['GET'])
def program_list_simple(request):
    queryset = Program.objects.all().prefetch_related('types')
    serializer = ProgramSerializer(queryset, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def program_list_with_routines(request):
    queryset = Program.objects.all().prefetch_related('types', 'programworkoutroutine_set',
                                                      'programworkoutroutine_set__workout')
    serializer = ProgramWithRoutinesSerializer(queryset, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def program_detail(request, program_id):
    try:
        program = Program.objects.prefetch_related('types').get(id=program_id)
    except Program.DoesNotExist:
        return Response({'error': 'Program not found'}, status=status.HTTP_404_NOT_FOUND)

    serializer = ProgramSerializer(program)
    return Response(serializer.data)


@api_view(['GET'])
def program_detail_with_routines(request, program_id):
    try:
        program = Program.objects.prefetch_related('types', 'programworkoutroutine_set',
                                                   'programworkoutroutine_set__workout').get(id=program_id)
    except Program.DoesNotExist:
        return Response({'error': 'Program not found'}, status=status.HTTP_404_NOT_FOUND)

    serializer = ProgramWithRoutinesSerializer(program)
    return Response(serializer.data)
