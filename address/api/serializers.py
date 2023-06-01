from rest_framework.serializers import ModelSerializer, StringRelatedField, PrimaryKeyRelatedField, SlugRelatedField, CharField, RelatedField
from address.models import Address, City, District, State



class StateSerializer(ModelSerializer):
    class Meta:
        model = State
        fields = ('id', 'name')


class CitySerializer(ModelSerializer):
    class Meta:
        model = City
        fields = ('id', 'name')
        deph=1


class DistrictSerializer(ModelSerializer):
    class Meta:
        model = District
        fields = ('id', 'name')
        deph=1


class AddressSerializer(ModelSerializer):       
    district = SlugRelatedField(slug_field=('name'), queryset=District.objects.all())
    city = SlugRelatedField(slug_field=('name'), queryset=City.objects.all())
    state = SlugRelatedField(slug_field=('name'), queryset=State.objects.all())
    class Meta:
        model = Address
        fields = ('id', 'street', 'district', 'city', 'state')
