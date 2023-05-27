from rest_framework.serializers import ModelSerializer, StringRelatedField, PrimaryKeyRelatedField, SlugRelatedField
from address.models import Address, City, District, State


class StateSerializer(ModelSerializer):
    class Meta:
        model = State
        fields = ('id', 'name')


class CitySerializer(ModelSerializer):
    class Meta:
        model = City
        fields = ('id', 'name')


class DistrictSerializer(ModelSerializer):
    class Meta:
        model = District
        fields = ('id', 'name')


class AddressSerializer(ModelSerializer):
    district = StringRelatedField()
    city = SlugRelatedField(slug_field='name', read_only=True)
    state = SlugRelatedField(slug_field='name', read_only=True)
    
    class Meta:
        model = Address
        fields = ('id', 'street', 'district', 'city', 'state')



