from http.client import PAYMENT_REQUIRED
from multiprocessing import context
from django.shortcuts import render,redirect
#from django.http import HttpResponse
from django.db.models import Q
from django.contrib import messages
from datetime import datetime
from datetime import datetime
from django.db.models import Max

#from tourandtravels.registration.admin import hoteladmin
from .models import  new_user
from hashlib import sha256
from .models import hotel,Vehicle,package,Vehicle_booking, Package_booking,Hotel_booking, Payment_Package
from .models import Payment_Bus,Payment_Hotel,Login,cancelations


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
            Login(username=username, password=password).save()
            return redirect('home')
        else:
            return redirect('login')
    return render(request,'login.html')

def logout(request):

    return render(request,'index.html')

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
    
    PNR_Number =  10010 if Vehicle_booking.objects.count() == 0 else Vehicle_booking.objects.aggregate(max=Max('PNR_id'))["max"] + int(1)
    
    if request.method == 'POST':
        name = request.POST.get('nm')
        seatno = request.POST.get('seatno')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        adhar_number = request.POST.get('adhar')
        total_amt = int(seatno) * int(seat_price)
        buses = Vehicle.objects.get(id=current_bus_id)
        buses.available_seats = int(buses.available_seats) - int(seatno)
        # current_blogin = Login.objects.latest('id').PNR_id
        # print(request.user)
        current_users = Login.objects.latest('username').username
        # print(current_users)
        if int(buses.available_seats) >= int(seatno):
           
            Vehicle_booking(Bus_id=vehicles.get(id=current_bus_id),PNR_id=PNR_Number,Passenger_name=name,Passenger_mobile=phone,Passenger_email=email,numberof_seats=seatno,adhar_number=adhar_number,total_rate=total_amt,current_user=current_users).save()
            buses.save()
            current_booking_id = Vehicle_booking.objects.latest('PNR_id').PNR_id
            
            
            return redirect('payments',current_bus_id,current_booking_id)
            #return render(request,'pyments.html',PNR_Number)
            
        else:
             messages.success(request,"No seats available")
            


    context = {
    }
    return render(request,'busbooking.html',context)

def Bus_payment(request,pk,PNR_id):

    vehicle_p1= Vehicle_booking.objects.all()

    current_bus_bookingid = id
    # print(current_bus_bookingid)
    current_PNR_id = PNR_id
    # print(current_PNR_id)
    #current_busid =   Vehicle_booking.objects.get(PNR_id=PNR_id).Bus_id_id 
    current_busprice =  Vehicle_booking.objects.get(PNR_id=PNR_id).total_rate
    if request.method == 'POST':
        Holder_name = request.POST.get('names')
        Card_number = request.POST.get('cardnumber')

        Year_valid = request.POST.get('year')
        Month_valid = request.POST.get('month')
        card_cvv = request.POST.get('cvv')
        print(card_cvv)

        
        Payment_Bus(Busbooking_id=vehicle_p1.get(PNR_id=current_PNR_id), Card_holdername= Holder_name, Card_number=Card_number, Valid_year=Year_valid,Valid_month=Month_valid,CVV=card_cvv,Total_amount=current_busprice).save()
        messages.success(request,"BOOKING DONE SUCCESSFULLY")
        return redirect('home')


    return render(request,'pyments.html')
    
def packagebooking(request,pk):
    Packagess = package.objects.all()
    current_package_id = package.objects.get(id=pk).id
    package_price = package.objects.get(id=pk).rate
    available_package_count = package.objects.get(id=pk).count

    PNR_P_Number =  20020 if Package_booking.objects.count() == 0 else Package_booking.objects.aggregate(max=Max('PNR_P_id'))["max"] + int(1)

    if request.method == 'POST':
        name = request.POST.get('names')
        mobile = request.POST.get('phone')
        email = request.POST.get('email')
        adhar = request.POST.get('adhar')
        number_adult = request.POST.get('adults')
        number_children = request.POST.get('childrens')
        packages_s = package.objects.get(id=current_package_id)
        packages_s.available_package = int(packages_s.available_package) - int(1)
        #new_avilable_package = package.objects.get(id=current_package_id).available_package
        #new_avilable_package_count = int(new_avilable_package) - int(1)
        current_users = Login.objects.latest('username').username

       
    
        if int(packages_s.available_package) > 0:
        #if int(new_avilable_package_count) <= int(available_package_count) & int(new_avilable_package_count) > 0:
            Package_booking(Package_id=Packagess.get(id=current_package_id),PNR_P_id=PNR_P_Number,Passenger_name=name,Passenger_mobile=mobile,Passenger_email=email,adhar_number=adhar,numberof_adult=number_adult,numberof_children=number_children,total_rate=package_price,current_user=current_users).save()
            packages_s.save()
            #package(available_package=new_avilable_package_count)

            current_booking_id_pack = Package_booking.objects.latest('PNR_P_id').PNR_P_id
            #return redirect('Package_payment')
            return redirect('payments_pka',current_package_id,current_booking_id_pack)
            # return render(request,'pyments.html')
        else:
            messages.success(request,"No Packages available")
    context = {
    }


    return render(request,'packagebooking.html')


def Package_payment(request,pk,PNR_P_id):
    Package_1=Package_booking.objects.all()

    current_PNR_P_id = PNR_P_id

    current_package_bookingid = id
    #current_packageid =  Package_booking.objects.get(id=pk).Package_id_id 
    current_packageprice = Package_booking.objects.get(PNR_P_id=PNR_P_id).total_rate
    if request.method == 'POST':
        Holder_name = request.POST.get('names')
        Card_number = request.POST.get('cardnumber')
        Year_valid = request.POST.get('year')
        Month_valid = request.POST.get('month')
        card_cvv = request.POST.get('cvv')

        
        Payment_Package(Packagebooking_id=Package_1.get(PNR_P_id=current_PNR_P_id),Card_holdername= Holder_name, Card_number=Card_number, Valid_year=Year_valid,Valid_month=Month_valid,CVV=card_cvv,Total_amount=current_packageprice).save()
        messages.success(request,"BOOKING DONE SUCCESSFULLY")
        return redirect('home')
        


    return render(request,'payment package.html')

#def numOfDays(checkin,checkout):
    #return (checkout-checkin).days

def hotelbooking(request,pk):
    Hotelss = hotel.objects.all()
    current_hotel_id = hotel.objects.get(id=pk).id
    room_price =  hotel.objects.get(id=pk).rate
    PNR_H_Number =  30030 if Hotel_booking.objects.count() == 0 else Hotel_booking.objects.aggregate(max=Max('PNR_H_id'))["max"] + int(1)

    if request.method == 'POST':
        name = request.POST.get('names')
        address = request.POST.get('address')
        mobile = request.POST.get('phone')
        email = request.POST.get('email')
        adhar = request.POST.get('adhar')
        checkin = request.POST.get('chekin')
        checkout = request.POST.get('checkout')
        rooms = request.POST.get('roomss')
        number_adult = request.POST.get('adult')
        number_children = request.POST.get('child')
        
        d1 = datetime.strptime(checkin, "%Y-%m-%d")
        d2 = datetime.strptime(checkout, "%Y-%m-%d")

        total_days = d2 - d1
        tot = total_days.days
        print(tot)
        total_amt = int(rooms) * int(room_price)  * int(tot)
        hotel_room = hotel.objects.get(id=current_hotel_id)
        hotel_room.available_rooms = int(hotel_room.available_rooms) - int(rooms)
        current_users = Login.objects.latest('username').username

        if int(hotel_room.available_rooms) >= int(rooms):
            Hotel_booking(Hotel_id=Hotelss.get(id=current_hotel_id),PNR_H_id=PNR_H_Number,User_name=name,User_address=address,User_mobile= mobile,User_email=email,User_adhar=adhar,Check_in=checkin,Check_out=checkout,numberof_rooms=rooms,numberof_adult=number_adult,numberof_children=number_children,total_rate=total_amt,current_user=current_users).save()
            hotel_room.save()
            current_booking_id = Hotel_booking.objects.latest('PNR_H_id').PNR_H_id
            return redirect('payments_hot',current_hotel_id,current_booking_id)

        else:
            messages.success(request,"No Rooms available")
            
        context = {
        }
       

   

    return render(request,'hotelbooking.html')

def Hotel_payment(request,pk,PNR_H_id):
    Hotels_1=Hotel_booking.objects.all()

    current_hotel_bookingid = id
    current_PNR_H_id = PNR_H_id
    #current_hotelid =  Hotel_booking.objects.get(id=pk).Package_id_id 
    current_hotelprice = Hotel_booking.objects.get(PNR_H_id=PNR_H_id).total_rate
    if request.method == 'POST':
        Holder_name = request.POST.get('names')
        Card_number = request.POST.get('cardnumber')
        Year_valid = request.POST.get('year')
        Month_valid = request.POST.get('month')
        card_cvv = request.POST.get('cvv')

        
        Payment_Hotel( Hotelbooking_id=Hotels_1.get(PNR_H_id=current_PNR_H_id),Card_holdername= Holder_name, Card_number=Card_number, Valid_year=Year_valid,Valid_month=Month_valid,CVV=card_cvv,Total_amount=current_hotelprice).save()
        messages.success(request,"BOOKING DONE SUCCESSFULLY")
        return redirect('home')



    return render(request,'payment hotel.html')

def index(request):

    return render(request,'index.html')

# def view_booking(request):
#     current_u = Login.objects.latest('id').id
#     curent_user_name = Login.objects.get(id=current_u).username
#     current_user_id = new_user.objects.get(username=curent_user_name).id
#     print(curent_user_name)
#     my_bookings = Vehicle_booking.objects.filter(current_user_id=current_user_id)
#     bus_id = Vehicle_booking.objects.get(current_user_id=current_user_id).Bus_id_id

#     bus_bookings = Vehicle.objects.filter(id=bus_id)
#     print(bus_bookings)
#     context = {
#         'my_bookings':my_bookings,
#         'bus_bookings' :bus_bookings
#     }

#     return render(request,'bookings.html',context)

def view_booking(request):
    current_users = Login.objects.latest('username').username

    if request.method == 'POST':
        pnrnumber=request.POST.get('firstname')
        booking_number=request.POST.get('booking number')
        mail_id=request.POST.get('mail id')
        cancelations(PNR_NUMBERS=pnrnumber,BOOKING_NUMBER=booking_number,email=mail_id,Current_user_man=current_users).save()
        return redirect('home')
    
    return render(request, 'bookings.html')
    

