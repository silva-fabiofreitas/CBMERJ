from django.contrib import admin
from django.urls import path, include

from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token 


from core.api import viewset as viewset_core
from epidemiological.api import viewset as viewset_epidemiological
from address.api import viewset as viewset_address
from event.api import viewset as viewset_event


router = routers.DefaultRouter()

router.register(r'endereco', viewset_address.AddressViewSet)
router.register(r'bairro', viewset_address.DistrictViewSet)
router.register(r'cidade', viewset_address.CityViewSet)
router.register(r'estado', viewset_address.StateViewSet)

router.register(r'perfil', viewset_epidemiological.ProfileViewSet)
router.register(r'genero', viewset_epidemiological.GenderViewSet)

router.register(r'risco', viewset_event.RiskRatingViewSet)
router.register(r'tipo-correncia', viewset_event.TypeOfOccurrenceViewSet)
router.register(r'tipo-acidente-transito', viewset_event.TypeOfTrafficAccidentViewSet)
router.register(r'tipo-unidade', viewset_event.UnitTypeViewSet)

router.register(r'registro-correncia', viewset_core.OcorrenceViewset)

urlpatterns = [
    path('', include(router.urls)),
    path('api/api-token-auth/', obtain_auth_token),
    path('api/api-auth/', include('rest_framework.urls')),
    path('api/accounts/', include('django.contrib.auth.urls')),
]
