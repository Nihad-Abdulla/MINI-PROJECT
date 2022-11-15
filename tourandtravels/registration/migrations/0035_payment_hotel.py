# Generated by Django 4.1.2 on 2022-11-12 15:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0034_new_user_password2'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment_Hotel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Card_holdername', models.CharField(max_length=20)),
                ('Card_number', models.IntegerField(null=True)),
                ('Valid_year', models.IntegerField(null=True)),
                ('Valid_month', models.CharField(max_length=20)),
                ('CVV', models.IntegerField(null=True)),
                ('Total_amount', models.IntegerField(null=True)),
                ('Hotelbooking_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registration.hotel_booking')),
            ],
        ),
    ]
