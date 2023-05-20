from rest_framework.serializers import ModelSerializer
from address.models import Address, City, District, State


class AddressSerializer(ModelSerializer):
    class Meta:
        model = Address
        fields = ('id', 'street', 'district', 'city')


class CitySerializer(ModelSerializer):
    class Meta:
        model = City
        fields = ('id', 'name', 'state')


class StateSerializer(ModelSerializer):
    class Meta:
        model = State
        fields = ('id', 'name')


class DistrictSerializer(ModelSerializer):
    class Meta:
        model = District
        fields = ('id', 'name')
