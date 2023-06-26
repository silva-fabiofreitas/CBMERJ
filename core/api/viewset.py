from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import PageNumberPagination

from core.models import Occurrence

from .serializers import OccurrenceSerializer


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 1000

class OcorrenceViewset(ModelViewSet):
    queryset = Occurrence.objects.all()
    serializer_class = OccurrenceSerializer
    pagination_class = StandardResultsSetPagination
