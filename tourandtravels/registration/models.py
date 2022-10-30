from email.mime import image
from unicodedata import name
from django.db import models

# Create your models here.
class new_user(models.Model):
    firstname=models.CharField(max_length=200)
    username=models.CharField(max_length=200)
    password=models.CharField(max_length=200)
    #password2=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    phone=models.CharField(max_length=200)
    question=models.CharField(max_length=200)
    answer=models.CharField(max_length=200)
    def __str__(self):
        return self.username

class login(models.Model):
    username=models.CharField(max_length=200)
    password=models.CharField(max_length=200)

class hotel(models.Model):
    name=models.CharField(max_length=200)
    place=models.CharField(max_length=200)
    image=models.ImageField(null=True, blank=False)
    description=models.CharField(max_length=200)
    roomtype=models.CharField(max_length=200)
    acnonac=models.CharField(max_length=200)
    count=models.IntegerField(max_length=200)
    rate=models.FloatField(max_length=200)

    def __str__(self):
        return self.place

class package(models.Model):
    packagetype=models.CharField(max_length=200)
    packagedetails=models.CharField(max_length=200)
    packagename=models.CharField(max_length=200)
    startingdate=models.DateField(max_length=200)
    endingdate=models.DateField(max_length=200)
    rate=models.CharField(max_length=200)
    image=models.ImageField(null=True, blank=False)

    
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
    count=models.IntegerField(max_length=200)
    price=models.CharField(max_length=200, null=True)
    available_seats=models.IntegerField(max_length=200,null=True)
    
    def __str__(self):
        return self.busname

class Vehicle_booking(models.Model):
    # user_id = models.ForeignKey(new_user,on_delete=models.CASCADE,default=0)
    Bus_id=models.ForeignKey(Vehicle,on_delete=models.CASCADE)
    Passenger_name=models.CharField(max_length=200)
    Passenger_mobile=models.IntegerField(max_length=10)
    Passenger_email=models.CharField(max_length=200)
    numberof_seats=models.IntegerField(max_length=200)
    adhar_number=models.CharField(max_length=200,null=True)
    total_rate=models.IntegerField(null=True)
    

   

