from rest_framework.serializers import ModelSerializer

from event.models import TypeOfOccurrence, RiskRating, TypeOfTrafficAccident, UnitType


class TypeOfOccurrenceSerializer(ModelSerializer):
    class Meta:
        model = TypeOfOccurrence
        fields = ('id', 'name')


class TypeOfTrafficAccidentSerializer(ModelSerializer):
    class Meta:
        model = TypeOfTrafficAccident
        fields = ('id', 'name')


class UnitTypeSerializer(ModelSerializer):
    class Meta:
        model = UnitType
        fields = ('id', 'name')


class RiskRatingSerializer(ModelSerializer):
    class Meta:
        model = RiskRating
        fields = ('id', 'rating')
