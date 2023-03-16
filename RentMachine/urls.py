from django.contrib import admin
from django.urls import path
from .views import RentMachine,UpdateRent

urlpatterns = [
    path("rentmachine/", RentMachine.as_view()),
  path("rentdata/<int:pk>", UpdateRent.as_view()),
]
