# Generated by Django 4.1.2 on 2022-11-17 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0050_alter_vehicle_booking_current_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cancelations',
            name='Current_user_man',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
