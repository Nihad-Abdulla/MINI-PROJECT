# Generated by Django 4.1.2 on 2022-11-14 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0040_remove_vehicle_booking_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicle_booking',
            name='PNR_id',
            field=models.IntegerField(null=True),
        ),
    ]
