from rest_framework.serializers import ModelSerializer, SlugRelatedField

from core.models import Occurrence
from epidemiological.api.serializers import ProfileSerializer
from address.api.serializers import AddressSerializer
from epidemiological.models import Profile

from event.models import RiskRating, UnitType, TypeOfOccurrence, TypeOfTrafficAccident
from address.models import Address


class OccurrenceSerializer(ModelSerializer):
    profile = ProfileSerializer()
    address = AddressSerializer()
    risk = SlugRelatedField(slug_field='rating', queryset=RiskRating.objects.all())
    type_of_occurrence = SlugRelatedField(slug_field='name', queryset=TypeOfOccurrence.objects.all())
    type_of_traffic_accident = SlugRelatedField(slug_field='name', queryset=TypeOfTrafficAccident.objects.all())
    unit_type = SlugRelatedField(slug_field='name', queryset=UnitType.objects.all())

    class Meta:
        model = Occurrence
        fields = '__all__'
    
    def create(self, validated_data):
        profile_data = validated_data.pop('profile')
        address_data = validated_data.pop('address')
        
        risk_data = validated_data.pop('risk')
        unit_type_data = validated_data.pop('unit_type')
        type_of_occurrence_data = validated_data.pop("type_of_occurrence")
        type_of_traffic_accident_data = validated_data.pop("type_of_traffic_accident")

        occurrence = Occurrence.objects.create(**validated_data)
        profile = Profile.objects.create(**profile_data)
        address = Address.objects.create(**address_data)

        occurrence.profile = profile
        occurrence.address = address
        occurrence.risk = risk_data
        occurrence.unit_type = unit_type_data
        occurrence.type_of_occurrence = type_of_occurrence_data
        occurrence.type_of_traffic_accident = type_of_traffic_accident_data
        occurrence.save()
        return occurrence
    
    def update(self,instance,validated_data):
        profile_data = validated_data.pop('profile')
        profile_serializer = self.fields['profile'] 
        profile_instance = instance.profile
        profile_serializer.update(profile_instance, profile_data)

        address_data = validated_data.pop('address')
        address_serializer = self.fields['address'] 
        address_instance = instance.address
        address_serializer.update(address_instance, address_data)

        instance.risk = validated_data.get('risk', instance.risk)
        instance.unit_type = validated_data.get('unit_type', instance.unit_type)
        instance.type_of_occurrence = validated_data.get("type_of_occurrence", instance.type_of_occurrence)
        instance.type_of_traffic_accident = validated_data.get("type_of_traffic_accident", instance.type_of_traffic_accident)

        return super(OccurrenceSerializer, self).update(instance, validated_data)
       

