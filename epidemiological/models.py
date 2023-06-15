from django.db import models
from django.utils.translation import gettext_lazy as _

class Profile(models.Model):
    class Gender(models.TextChoices):
        MALE = 'ME', _('Masculino')
        FEMELE = 'FE', _('Feminino')

    age = models.PositiveSmallIntegerField(default=0, blank=True, null=True)
    gender = models.CharField(max_length=2, choices=Gender.choices)

    def __str__(self):
        return f'Age {self.age} Gender {self.gender}'
   
