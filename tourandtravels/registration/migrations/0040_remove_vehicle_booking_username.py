# Generated by Django 4.1.2 on 2022-11-14 10:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0039_vehicle_booking_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vehicle_booking',
            name='username',
        ),
    ]
