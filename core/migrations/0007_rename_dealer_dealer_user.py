# Generated by Django 4.1.7 on 2023-03-18 16:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_rename_user_dealer_dealer'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dealer',
            old_name='dealer',
            new_name='user',
        ),
    ]