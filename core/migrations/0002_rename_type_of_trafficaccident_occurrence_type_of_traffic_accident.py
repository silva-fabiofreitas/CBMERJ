# Generated by Django 4.2.1 on 2023-06-17 19:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='occurrence',
            old_name='type_of_trafficaccident',
            new_name='type_of_traffic_accident',
        ),
    ]
