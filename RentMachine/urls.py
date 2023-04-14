from django.contrib import admin
from django.urls import path
from .views import RentMachine,UpdateRent,UserRent


urlpatterns = [
  path("rentmachine/", RentMachine.as_view()),
  path("rentdata/<int:pk>", UpdateRent.as_view()),
 path("rentdatauser/<int:pk>", UserRent.as_view()), 
]
