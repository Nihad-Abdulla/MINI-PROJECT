# Generated by Django 4.1.2 on 2022-11-17 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0052_alter_cancelations_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotel_booking',
            name='current_user',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='package_booking',
            name='current_user',
            field=models.CharField(max_length=200, null=True),
        ),
    ]