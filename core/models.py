from django.db import models

from address.models import Address
from epidemiological.models import Profile
from event.models import (
    RiskRating, TypeOfOccurrence, TypeOfTrafficAccident, UnitType
)


class Occurrence(models.Model):
    date = models.DateTimeField()
    address = models.ForeignKey(Address)
    profile = models.ForeignKey(Profile)
    risk = models.ForeignKey(RiskRating)
    unit_type = models.ForeignKey(UnitType)
    type_of_occurrence = models.ForeignKey(TypeOfOccurrence)
    type_of_trafficaccident = models.ForeignKey(TypeOfTrafficAccident)

    def __str__(self) -> str:
        return f'{self.date} - {self.risk}'
