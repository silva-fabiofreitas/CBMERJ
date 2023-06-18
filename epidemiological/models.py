from django.db import models
from django.utils.translation import gettext_lazy as _


class Gender(models.Model):
    class Type(models.TextChoices):
        MALE = 'ME', _('Masculino')
        FEMELE = 'FE', _('Feminino')
        
    name = models.CharField(max_length=255, choices=Type.choices)

    def __str__(self) -> str:
        return self.name
    

class Profile(models.Model):
    age = models.PositiveSmallIntegerField(default=0, blank=True, null=True)
    gender = models.ForeignKey(Gender, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f'Age {self.age} Gender {self.gender}'
   
