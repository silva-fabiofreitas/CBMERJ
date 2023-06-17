from rest_framework.viewsets import ModelViewSet

from event.models import (RiskRating,
                          TypeOfOccurrence,
                          TypeOfTrafficAccident,
                          UnitType)

from .serializers import (TypeOfOccurrenceSerializer,
                          TypeOfTrafficAccidentSerializer,
                           UnitTypeSerializer,
                           RiskRatingSerializer)


class TypeOfOccurrenceViewSet(ModelViewSet):
    queryset = TypeOfOccurrence.objects.all()
    serializer_class = TypeOfOccurrenceSerializer


class TypeOfTrafficAccidentViewSet(ModelViewSet):
    queryset = TypeOfTrafficAccident.objects.all()
    serializer_class = TypeOfTrafficAccidentSerializer


class UnitTypeViewSet(ModelViewSet):
    queryset = UnitType.objects.all()
    serializer_class = UnitTypeSerializer


class RiskRatingViewSet(ModelViewSet):
    queryset = RiskRating.objects.all()
    serializer_class = RiskRatingSerializer