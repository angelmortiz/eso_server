from rest_framework.viewsets import ModelViewSet

from ..models import Muscle
from ..serializers import MuscleSerializer


class MuscleViewSet(ModelViewSet):
    queryset = Muscle.objects.all()
    serializer_class = MuscleSerializer
