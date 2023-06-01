from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.authentication import TokenAuthentication
from address.models import Address, City, State, District
from .serializers import AddressSerializer, CitySerializer, StateSerializer, DistrictSerializer
from rest_framework.decorators import action


class AddressViewSet(ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer


class CityViewSet(ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer


class StateViewSet(ModelViewSet):
    queryset = State.objects.all()
    serializer_class = StateSerializer

class DistrictViewSet(ModelViewSet):
    queryset = District.objects.all()
    serializer_class = DistrictSerializer