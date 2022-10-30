from django.contrib import admin
from django.urls import path,include,re_path
from .import views
#from django.conf.urls import re_path
urlpatterns = [
    path('',views.index,name='index'),
    path('register/',views.register,name='register'),
    path('login/',views.login,name='login'),
    path('home/',views.home,name='home'),
    path('hotels/',views.hotels,name='hotels'),
    path('hotels/<int:pk>',views.hotels_individual,name='hotels_individual'),
    path('bus/',views.bus,name='bus'),
    path('bus/<int:pk>',views.bus_individuals,name='bus_individuals'),
    path('packagesearch/',views.search_package,name='search_package'),
    path('packagesearch/<int:pk>',views.package_individuals,name='package_individuals'),
    path('bus/<int:pk>/busbooking/',views.busbooking,name='busbooking'),
    path('packagebooking/',views.packagebooking,name='packagebooking'),
    path('hotelbooking/',views.hotelbooking,name='hotelbooking'),


]
