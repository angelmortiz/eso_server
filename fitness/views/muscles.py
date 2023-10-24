from rest_framework.filters import SearchFilter
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend

from ..models import Muscle
from ..pagination import DefaultPagination
from ..serializers import MuscleSerializer


class MuscleViewSet(ModelViewSet):
    queryset = Muscle.objects.all()
    serializer_class = MuscleSerializer
    # Filters
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['type']
    search_fields = ['name', 'alternative_name']
    # Pagination
    pagination_class = DefaultPagination
