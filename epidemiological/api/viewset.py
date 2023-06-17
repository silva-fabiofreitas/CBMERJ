from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action

from .serializers import ProfileSerializer
from epidemiological.models import Profile


class ProfileViewSet(ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
