from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import PageNumberPagination
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status

from core.models import Occurrence
from core.service.statistic import Dashboard

from .serializers import OccurrenceSerializer


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 1000

class OcorrenceViewset(ModelViewSet):
    queryset = Occurrence.objects.all()
    serializer_class = OccurrenceSerializer
    pagination_class = StandardResultsSetPagination
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ('profile__gender__name', 'risk', 'unit_type', 'type_of_occurrence', 'type_of_traffic_accident', 'date')


    @action(detail=False, methods=['get'])
    def get_pie_charts(self, request, pk=None):
        '''
        Retorna os tipos de ocorrencia.
        '''
    
        qs = self.filter_queryset(self.get_queryset())
        Dashboard.setFilteredOccurrence(qs)
        result = Dashboard.get_statistc_piechart()
        
        return Response(result, status=status.HTTP_200_OK)


    @action(detail=False, methods=['get'])
    def get_histogram_charts(self, request, pk=None):
        '''
        Retorna os tipos de ocorrencia.
        '''
    
        qs = self.filter_queryset(self.get_queryset())
        Dashboard.setFilteredOccurrence(qs)
        result = Dashboard.get_age()
        
        return Response(result, status=status.HTTP_200_OK)
      