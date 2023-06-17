from rest_framework.viewsets import ModelViewSet

from core.models import Occurrence

from .serializers import OccurrenceSerializer


class OcorrenceViewset(ModelViewSet):
    queryset = Occurrence.objects.all()
    serializer_class = OccurrenceSerializer
