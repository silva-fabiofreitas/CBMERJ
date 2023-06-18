from rest_framework.serializers import ModelSerializer, SlugRelatedField
from ..models import Profile, Gender


class ProfileSerializer(ModelSerializer):
    gender = SlugRelatedField(slug_field='name', queryset=Gender.objects.all())

    class Meta:
        model = Profile
        fields = ('id', 'age', 'gender')

class GenderSerializer(ModelSerializer):
    class Meta:
        model = Gender
        fields = ('id', 'name')
