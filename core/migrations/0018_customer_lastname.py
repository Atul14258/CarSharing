# Generated by Django 4.1.7 on 2023-03-22 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0017_customer_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='lastname',
            field=models.CharField(default=False, max_length=100),
        ),
    ]