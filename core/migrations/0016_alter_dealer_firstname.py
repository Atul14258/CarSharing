# Generated by Django 4.1.7 on 2023-03-22 04:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_dealer_email_dealer_firstname_dealer_lastname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dealer',
            name='firstname',
            field=models.CharField(max_length=100),
        ),
    ]