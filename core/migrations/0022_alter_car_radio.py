# Generated by Django 4.1.1 on 2023-03-25 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0021_car_radio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='radio',
            field=models.BooleanField(default=True),
        ),
    ]