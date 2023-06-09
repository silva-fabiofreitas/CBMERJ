from django.db import models


class District(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class State(models.Model):
    name = models.CharField(max_length=100, unique=True)

    @property
    def full_name(self):
        return f'{self.id} - {self.name}'

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name
    

class Address(models.Model):
    street = models.CharField(max_length=255)
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    state = models.ForeignKey(State, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.street}, {self.district}, {self.city}'
    