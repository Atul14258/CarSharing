# Generated by Django 4.1.1 on 2023-03-25 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0020_alter_dealer_firstname'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='radio',
            field=models.CharField(default=False, max_length=100),
        ),
    ]