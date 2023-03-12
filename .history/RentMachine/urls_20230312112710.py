from django.contrib import admin
from django.urls import path
from .views import RentMachine

urlpatterns = [
    path("rentmachine/", RentrMachine.as_view()),
]
