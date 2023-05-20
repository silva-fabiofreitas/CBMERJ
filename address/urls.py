from django.urls import include, path

from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token 

from .api import viewset


router = routers.DefaultRouter()

router.register(r'endereco', viewset.AddressViewSet)
router.register(r'bairro', viewset.DistrictViewSet)
router.register(r'cidade', viewset.CityViewSet)
router.register(r'estado', viewset.StateViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/api-token-auth/', obtain_auth_token),
    path('api/api-auth/', include('rest_framework.urls')),
    path('api/accounts/', include('django.contrib.auth.urls')),
]
