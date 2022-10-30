from multiprocessing import context
from django.shortcuts import render,redirect
#from django.http import HttpResponse
from django.db.models import Q

#from tourandtravels.registration.admin import hoteladmin
from .models import  new_user
from hashlib import sha256
from .models import hotel,Vehicle,package,Vehicle_booking



# Create your views here.
def register(request):
    if request.method == 'POST':
        firstname=request.POST.get('firstname')
        username=request.POST.get('username')
        password=request.POST.get('password')
        password2=request.POST.get('password2')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        question=request.POST.get('question')
        answer=request.POST.get('answer')
        new_user(firstname=firstname,username=username,password=password,password2=password2,email=email,phone=phone,question=question,answer=answer).save()
    return render(request, 'registration.html')

def login(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        Password1=sha256(password.encode()).hexdigest()
        user=new_user.objects.filter(username=username,password=password)
        if user:
            return redirect('home')
        else:
            return redirect('login')
    return render(request,'login.html')
def home(request):

    return render(request,'home.html')

def hotels(request):
     if 'q' in request.GET:
         q = request.GET['q']
         Hotel = hotel.objects.filter(place__icontains=q)
     else:
         Hotel = hotel.objects.all()
     context = {
        'Hotel': Hotel
    }
   
     return render(request,'hotel.html',context)
def hotels_individual(request ,pk):
     individuals = hotel.objects.get(id=pk)
     context = {
        'individuals':individuals
    }
   
     return render(request,'hotel_individuals.html',context)
def bus(request):
    if 'w' and 'x' and 'q' in request.GET:
        w = request.GET['w']
        x = request.GET['x']
        q = request.GET['q']
        buses = Vehicle.objects.filter(Q(source__icontains=w) & Q(destination__icontains=x) & Q(date__icontains=q) )
    else:
        buses = Vehicle.objects.all()
    context = {
    'buses': buses
    }

    return render(request, 'bus.html',context)
def bus_individuals(request ,pk):
     individuals = Vehicle.objects.get(id=pk)
     context = {
        'individuals':individuals
    }
   
     return render(request,'bus_individuals.html',context)

def search_package(request):
    if 'w' and 'q' in request.GET:
        w = request.GET['w']
        q = request.GET['q']
        new_package = package.objects.filter(Q(packagename__icontains=w) & Q(packagetype__icontains=q))
    else:
        new_package = package.objects.all()
    context = {
    'new_package': new_package
    }

    return render(request, 'package.html',context)
    
def package_individuals(request ,pk):
     individuals = package.objects.get(id=pk)
     context = {
        'individuals':individuals
    }
   
     return render(request,'package_individuals.html',context)




def busbooking(request,pk):
    vehicles = Vehicle.objects.all()
    current_bus_id = Vehicle.objects.get(id=pk).id
    seat_price =  Vehicle.objects.get(id=pk).price
    # user_id = request.user.id
    # print("hjdfds",user_id)
    if request.method == 'POST':
        name = request.POST.get('nm')
        seatno = request.POST.get('seatno')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        total_amt = int(seatno) * int(seat_price)

        Vehicle_booking(Bus_id=vehicles.get(id=current_bus_id),Passenger_name=name,Passenger_mobile=phone,Passenger_email=email,numberof_seats=seatno,total_rate=total_amt).save()



    context = {
    }
    return render(request,'busbooking.html',context)

    
def packagebooking(request):

    return render(request,'packagebooking.html')

def hotelbooking(request):

    return render(request,'hotelbooking.html')

def index(request):

    return render(request,'index.html')


