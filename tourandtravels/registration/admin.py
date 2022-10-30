from ast import Div
from django.contrib import admin
from .models import Vehicle_booking, hotel,Vehicle,package, new_user




# Register your models here.
admin.site.register(new_user),
admin.site.register(hotel),
admin.site.register(Vehicle),
admin.site.register(package),
admin.site.register(Vehicle_booking),
