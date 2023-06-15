from django.contrib import admin
from django.urls import path, include

from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token 



from epidemiological.api import viewset as viewset_epidemiological
from address.api import viewset as viewset_address


router = routers.DefaultRouter()

router.register(r'endereco', viewset_address.AddressViewSet)
router.register(r'bairro', viewset_address.DistrictViewSet)
router.register(r'cidade', viewset_address.CityViewSet)
router.register(r'estado', viewset_address.StateViewSet)

router.register(r'perfil', viewset_epidemiological.ProfileViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api/api-token-auth/', obtain_auth_token),
    path('api/api-auth/', include('rest_framework.urls')),
    path('api/accounts/', include('django.contrib.auth.urls')),
]
