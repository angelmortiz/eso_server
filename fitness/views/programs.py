from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from ..models import Program
from ..serializers import ProgramSerializer


@api_view(['GET'])
def program_list(request):
    queryset = Program.objects.all()
    serializer = ProgramSerializer(queryset, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def program_detail(request, program_id):
    program = get_object_or_404(Program, id=program_id)
    serializer = ProgramSerializer(program)
    return Response(serializer.data)
