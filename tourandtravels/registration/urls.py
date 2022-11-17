from django.contrib import admin
from django.urls import path,include,re_path
from .import views
#from django.conf.urls import re_path
urlpatterns = [
    path('',views.index,name='index'),
    path('register/',views.register,name='register'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    path('home/',views.home,name='home'),
    path('hotels/',views.hotels,name='hotels'),
    path('bookings/',views.view_booking,name='bookings'),
    path('hotels/<int:pk>',views.hotels_individual,name='hotels_individual'),
    path('bus/',views.bus,name='bus'),
    path('bus/<int:pk>',views.bus_individuals,name='bus_individuals'),
    path('packagesearch/',views.search_package,name='search_package'),
    path('packagesearch/<int:pk>',views.package_individuals,name='package_individuals'),
    path('bus/<int:pk>/busbooking/',views.busbooking,name='busbooking'),
    path('bus/<int:pk>/busbooking/<PNR_id>/payments',views.Bus_payment,name='payments'),
    path('packagesearch/<int:pk>/packagebooking/',views.packagebooking,name='packagebooking'),
    path('packagesearch/<int:pk>/packagebooking/<PNR_P_id>/payments_pka',views.Package_payment,name='payments_pka'),
    path('hotels/<int:pk>/hotelbooking/',views.hotelbooking,name='hotelbooking'),
    path('hotels/<int:pk>/hotelbooking/<PNR_H_id>/payments_hot',views.Hotel_payment,name='payments_hot')
    # path('packagesearch/<int:pk>/packagebooking/Package_payment',views.Bus_payment,name='Package_payment'),
]
