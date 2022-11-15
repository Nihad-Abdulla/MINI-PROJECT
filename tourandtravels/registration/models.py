from email.mime import image
from unicodedata import name
from django.db import models

# Create your models here.
class new_user(models.Model):
    firstname=models.CharField(max_length=200)
    username=models.CharField(max_length=200)
    password=models.CharField(max_length=200)
    password2=models.CharField(max_length=200,null=True)
    email=models.CharField(max_length=200)
    phone=models.CharField(max_length=200)
    question=models.CharField(max_length=200)
    answer=models.CharField(max_length=200)
    def __str__(self):
        return self.username

class Login(models.Model):
    username=models.CharField(max_length=200)
    password=models.CharField(max_length=200)

class hotel(models.Model):
    name=models.CharField(max_length=200)
    place=models.CharField(max_length=200)
    image=models.ImageField(null=True, blank=False)
    description=models.TextField(max_length=1000)
    roomtype=models.CharField(max_length=200)
    acnonac=models.CharField(max_length=200)
    count=models.IntegerField(null=True)
    rate=models.FloatField(max_length=200)
    available_rooms=models.IntegerField(null=True)

    def __str__(self):
        return self.place

class package(models.Model):
    packagetype=models.CharField(max_length=200)
    packagedetails=models.TextField(max_length=1000)
    packagename=models.CharField(max_length=200)
    startingdate=models.DateField(max_length=200)
    endingdate=models.DateField(max_length=200)
    rate=models.CharField(max_length=200)
    image=models.ImageField(null=True, blank=False)
    count=models.IntegerField(null=True)
    available_package=models.IntegerField(null=True)

    
    def __str__(self):
        return self.packagename
    

class Vehicle(models.Model):
    busname=models.CharField(max_length=200, null=True)
    date=models.DateField(max_length=200)
    source=models.CharField(max_length=200)
    destination=models.CharField(max_length=200)
    startingtime=models.CharField(max_length=200)
    endingtime=models.CharField(max_length=200)
    bustype=models.CharField(max_length=200)
    count=models.IntegerField(null=True)
    price=models.CharField(max_length=200, null=True)
    available_seats=models.IntegerField(null=True)
    image=models.ImageField(null=True, blank=False)
    
    def __str__(self):
        return self.busname

class Vehicle_booking(models.Model):
    PNR_id=models.IntegerField(null=True)
    Bus_id=models.ForeignKey(Vehicle,on_delete=models.CASCADE)
    Passenger_name=models.CharField(max_length=200)
    Passenger_mobile=models.IntegerField(null=True)
    Passenger_email=models.CharField(max_length=200)
    numberof_seats=models.IntegerField(null=True)
    adhar_number=models.CharField(max_length=200,null=True)
    total_rate=models.IntegerField(null=True)

class Package_booking(models.Model):
    PNR_P_id=models.IntegerField(null=True)
    Package_id=models.ForeignKey(package,on_delete=models.CASCADE)
    Passenger_name=models.CharField(max_length=200)
    Passenger_mobile=models.IntegerField(null=True)
    Passenger_email=models.CharField(max_length=200)
    adhar_number=models.CharField(max_length=200,null=True)
    numberof_adult=models.IntegerField(null=True)
    numberof_children=models.IntegerField(null=True)
    total_rate=models.IntegerField(null=True)

class Hotel_booking(models.Model):
    PNR_H_id=models.IntegerField(null=True)
    Hotel_id=models.ForeignKey(hotel,on_delete=models.CASCADE)
    User_name=models.CharField(max_length=200)
    User_address=models.CharField(max_length=200)
    User_mobile=models.IntegerField(null=True)
    User_email=models.CharField(max_length=200)
    User_adhar=models.IntegerField(null=True)
    Check_in=models.DateField(null=True)
    Check_out=models.DateField(null=True)
    numberof_rooms=models.IntegerField(null=True)
    numberof_adult=models.IntegerField(null=True)
    numberof_children=models.IntegerField(null=True)
    total_rate=models.IntegerField(null=True)



class Payment_Bus(models.Model):
    Vehicle_id=models.ForeignKey(Vehicle,on_delete=models.CASCADE)
    Busbooking_id=models.ForeignKey(Vehicle_booking,on_delete=models.CASCADE)
    Card_holdername=models.CharField(max_length=20)
    Card_number=models.IntegerField(null=True)
    Valid_year=models.IntegerField(null=True)
    Valid_month=models.CharField(max_length=20)
    Total_amount=models.ImageField(null=True)

class Payment_Package(models.Model):
    #Package_id=models.ForeignKey(package,on_delete=models.CASCADE)
    Packagebooking_id=models.ForeignKey(Package_booking,on_delete=models.CASCADE)
    Card_holdername=models.CharField(max_length=20)
    Card_number=models.IntegerField(null=True)
    Valid_year=models.IntegerField(null=True)
    Valid_month=models.CharField(max_length=20)
    CVV=models.IntegerField(null=True)
    Total_amount=models.IntegerField(null=True)

class Payment_Hotel(models.Model):
    #Package_id=models.ForeignKey(package,on_delete=models.CASCADE)
    Hotelbooking_id=models.ForeignKey(Hotel_booking,on_delete=models.CASCADE)
    Card_holdername=models.CharField(max_length=20)
    Card_number=models.IntegerField(null=True)
    Valid_year=models.IntegerField(null=True)
    Valid_month=models.CharField(max_length=20)
    CVV=models.IntegerField(null=True)
    Total_amount=models.IntegerField(null=True)


    

   

