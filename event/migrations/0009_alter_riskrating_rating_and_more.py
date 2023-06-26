# Generated by Django 4.2.1 on 2023-06-22 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0008_alter_riskrating_rating_alter_typeofoccurrence_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='riskrating',
            name='rating',
            field=models.CharField(choices=[('Azul', 'Não Urgente'), ('Verde', 'Pouco Urgente'), ('Amarelo', 'Urgente'), ('Laranja', 'Muito Urgente'), ('Vermelho', 'Emergente'), ('Outros', 'Outros')], max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='typeoftrafficaccident',
            name='name',
            field=models.CharField(choices=[('------', '------'), ('Atropelamento', 'Atropelamento'), ('Capotamento', 'Capotamento'), ('Colisão', 'Colisão'), ('Queda Bicicleta', 'Queda Bicicleta'), ('Queda Moto', 'Queda Moto'), ('Outros', 'Outros')], max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='unittype',
            name='name',
            field=models.CharField(choices=[('------', '------'), ('Avançada', 'Avançada'), ('Intermediaria', 'Intermediaria'), ('Basica', 'Basica')], max_length=100, unique=True),
        ),
    ]