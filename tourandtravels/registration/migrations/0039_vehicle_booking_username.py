# Generated by Django 4.1.2 on 2022-11-14 09:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0038_vehicle_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicle_booking',
            name='username',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='registration.login'),
        ),
    ]
