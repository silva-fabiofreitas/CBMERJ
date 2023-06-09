from django.db import models

# Create your models here.


class RiskRating(models.Model):
    "Modelo de classificação de risco"
    class Risk(models.TextChoices):
        "Enum"
        AZUL =  'Azul', 'Não Urgente',
        VERDE =  'Verde', 'Pouco Urgente',
        AMARELO =  'Amarelo', 'Urgente',
        LARANJA =  'Laranja', 'Muito Urgente',
        VERMELHO =  'Vermelho', 'Emergente',
        OUTROS = 'Outros', 'Outros'

    rating = models.CharField(max_length=100, choices=Risk.choices, unique=True)

    def __str__(self) -> str:
        return f'{self.rating}'


class TypeOfOccurrence(models.Model):
    "Modelo de tipo de ocorrência EV CARACT"
    class Type(models.TextChoices):
        "Enum"
        ACIDENTE = 'Acidente e Violencia', 'Acidente e Violência'
        CLINICO = 'Clinico', 'Clinico'
        OBSTETRICO = 'Obstétrico', 'Obstétrico'
        PSIQUIATRICO = 'Psiquiatrico', 'Psiquiatrico'
        OUTROS = 'Outros', 'Outros'

    name = models.CharField(
        max_length=100, choices=Type.choices, unique=True)

    def __str__(self) -> str:
        return f'{self.name}'


class TypeOfTrafficAccident(models.Model):
    "Modelo de tipo de ocorrência AC TRANSP"
    class Type(models.TextChoices):
        "Enum"
        VAZIO = '------', '------'
        ATROPELAMENTO = 'Atropelamento', 'Atropelamento'
        CAPOTAMENTO = 'Capotamento', 'Capotamento'
        COLISAO = 'Colisão', 'Colisão'
        QUEDA_BICICLETA = 'Queda Bicicleta', 'Queda Bicicleta'
        QUEDA_MOTO = 'Queda Moto', 'Queda Moto'
        OUTROS = 'Outros', 'Outros'

    name = models.CharField(
        max_length=100, choices=Type.choices, unique=True)

    def __str__(self) -> str:
        return f'{self.name}'


class UnitType(models.Model):
    "Configuração da unidade de atendimento"
    class Type(models.TextChoices):
        "Enum"
        VAZIO = '------', '------'
        ADVANCED = 'Avançada', 'Avançada'
        INTERMEDIATE = 'Intermediária', 'Intermediária'
        BASIC = 'Básica', 'Básica'

    name = models.CharField(
        max_length=100, choices=Type.choices, unique=True)

    def __str__(self) -> str:
        return f'{self.name}'
