from django.db import models

# Create your models here.


class RiskRating(models.Model):
    "Modelo de classificação de risco"
    class Risk(models.TextChoices):
        AZUL = 'Azul', 'Não Urgente'
        VERDE = 'Verde', 'Pouco Urgente'
        AMARELO = 'Amarelo', 'Urgente'
        LARANJA = 'Laranja', 'Muito Urgente'
        VERMELHO = 'Vermelho', 'Emergente'
        OUTROS = 'Outros', 'Outros'

    rating = models.CharField(max_length=100, choices=Risk.choices)

    def __str__(self) -> str:
        return f'{self.rating}'


class typeOfOccurrence(models.Model):
    "Modelo de tipo de ocorrência EV CARACT"
    class Type(models.TextChoices):
        ACIDENTE = 'Acidente e Violencia', 'Acidente E Violencia'
        CLINICO = 'Clinico', 'Clinico'
        N_PREENC = 'N.Preenc', 'N.Preenc'
        OBSTETRICO = 'Obstétrico', 'Obstétrico'
        OUTROS = 'Outros', 'Outros'
        PSIQUIATRICO = 'Psiquiatrico', 'Psiquiatrico'

    name = models.CharField(
        max_length=100, choices=Type.choices, blank=True, null=True)

    def __str__(self) -> str:
        return f'{self.name}'


class TypeOfTrafficAccident(models.Model):
    "Modelo de tipo de ocorrência AC TRANSP"
    class Type(models.TextChoices):
        ATROPELAMENTO = 'Atropelamento', 'Atropelamento'
        CAPOTAMENTO = 'Capotamento', 'Capotamento'
        COLISAO = 'Colisão', 'Colisão'
        IGNORADO = 'Ignorado', 'Ignorado'
        N_PREENC = 'N.Preenc', 'N.Preenc'
        OUTROS = 'Outros', 'Outros'
        QUEDA_BICICLETA = 'Queda Bicicleta', 'Queda Bicicleta'
        QUEDA_MOTO = 'Queda Moto', 'Queda Moto'

    name = models.CharField(
        max_length=100, choices=Type.choices, blank=True, null=True)

    def __str__(self) -> str:
        return f'{self.name}'


class UnitType(models.Model):
    "Configuração da unidade de atendimento"
    class Type(models.TextChoices):
        ADVANCED = 'Avançada', 'Avançada'
        INTERMEDIATE = 'Intermediaria', 'Intermediaria'
        BASIC = 'Basica', 'Basica'

    name = models.CharField(
        max_length=100, choices=Type.choices, blank=True, null=True)

    def __str__(self) -> str:
        return f'{self.name}'
