# Generated by Django 4.1.2 on 2022-11-12 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0035_payment_hotel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotel',
            name='description',
            field=models.TextField(max_length=200),
        ),
    ]
