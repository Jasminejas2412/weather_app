# Generated by Django 4.2.6 on 2023-11-13 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weatherApp', '0004_alter_weather_celsius_temperature'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weather',
            name='celsius_temperature',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='weather',
            name='kelvin_temperature',
            field=models.IntegerField(null=True),
        ),
    ]
