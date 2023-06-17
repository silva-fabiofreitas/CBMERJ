from django.db import models

from address.models import Address
from epidemiological.models import Profile
from event.models import (
    RiskRating, TypeOfOccurrence, TypeOfTrafficAccident, UnitType
)


class Occurrence(models.Model):
    date = models.DateTimeField()
    address = models.ForeignKey(Address, on_delete=models.SET_NULL, blank=True, null=True)
    profile = models.ForeignKey(Profile, on_delete=models.SET_NULL, blank=True, null=True)
    risk = models.ForeignKey(RiskRating, on_delete=models.SET_NULL, blank=True, null=True)
    unit_type = models.ForeignKey(UnitType, on_delete=models.SET_NULL, blank=True, null=True)
    type_of_occurrence = models.ForeignKey(TypeOfOccurrence, on_delete=models.SET_NULL, blank=True, null=True)
    type_of_trafficaccident = models.ForeignKey(TypeOfTrafficAccident, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self) -> str:
        return f'{self.date} - {self.risk}'
