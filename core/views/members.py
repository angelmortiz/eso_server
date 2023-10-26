from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.viewsets import ModelViewSet

from ..models import Member
from ..serializers import MemberSerializer


class MemberViewSet(ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer

    # Permissions
    permission_classes = [IsAdminUser]

    @action(detail=False, methods=['GET', 'PUT', 'PATCH'], permission_classes=[IsAuthenticated])
    def me(self, request: Request) -> Response:
        member = Member.objects.select_related('user').get(user=request.user)
        if request.method == 'GET':
            serializer = MemberSerializer(member)
            return Response(serializer.data)
        elif request.method == 'PUT' or request.method == 'PATCH':
            serializer = MemberSerializer(member, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)
