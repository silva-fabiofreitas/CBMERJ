# Generated by Django 4.2.1 on 2023-06-18 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0006_alter_riskrating_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='typeofoccurrence',
            name='name',
            field=models.CharField(choices=[('------', '------'), ('Acidente e Violencia', 'Acidente e Violência'), ('Clinico', 'Clinico'), ('Obstétrico', 'Obstétrico'), ('Psiquiatrico', 'Psiquiatrico'), ('Outros', 'Outros')], max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='typeoftrafficaccident',
            name='name',
            field=models.CharField(choices=[('------', '------'), ('Atropelamento', 'Atropelamento'), ('Capotamento', 'Capotamento'), ('Colisão', 'Colisão'), ('Queda Bicicleta', 'Queda Bicicleta'), ('Queda Moto', 'Queda Moto'), ('Outros', 'Outros')], max_length=100, unique=True),
        ),
    ]