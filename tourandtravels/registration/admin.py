from ast import Div
from django.contrib import admin
from .models import Vehicle_booking, hotel,Vehicle,package, new_user,Package_booking,Payment_Bus,Payment_Package
from .models import Hotel_booking,Payment_Hotel,Login



# Register your models here.
admin.site.register(new_user),
admin.site.register(hotel),
admin.site.register(Login),
admin.site.register(Vehicle),
admin.site.register(package),
admin.site.register(Vehicle_booking),
admin.site.register(Package_booking),
admin.site.register(Hotel_booking),
admin.site.register(Payment_Bus),
admin.site.register(Payment_Package),
admin.site.register(Payment_Hotel),