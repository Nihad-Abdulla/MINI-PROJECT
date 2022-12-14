# Generated by Django 4.1.2 on 2022-11-01 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0023_alter_package_booking_passenger_mobile_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='package_booking',
            name='total_rate',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='available_seats',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='vehicle_booking',
            name='total_rate',
            field=models.IntegerField(null=True),
        ),
    ]
