from django.contrib import admin
from django.urls import path
from .views import RentMachine,UpdateRent,UserRent,Orderss


urlpatterns = [
  path("rentmachine/", RentMachine.as_view()),
  path("rentdata/<int:pk>", UpdateRent.as_view()),
 path("rentdatauser/<int:pk>", UserRent.as_view()), 
 path("rentinfo", Orderss.as_view() )
]
