# Generated by Django 4.0.6 on 2022-07-18 18:34

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('TeamManagement', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teammember',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, region='CA'),
        ),
    ]
