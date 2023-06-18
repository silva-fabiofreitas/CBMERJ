from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action

from .serializers import ProfileSerializer, GenderSerializer
from epidemiological.models import Profile, Gender


class ProfileViewSet(ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class GenderViewSet(ModelViewSet):
    queryset = Gender.objects.all()
    serializer_class = GenderSerializer