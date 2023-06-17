from rest_framework.serializers import ModelSerializer
from core.models import Occurrence

class OccurrenceSerializer(ModelSerializer):
    class Meta:
        model = Occurrence
        fields = '__all__'

