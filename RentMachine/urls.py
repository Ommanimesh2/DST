from django.contrib import admin
from django.urls import path
from .views import RentMachine

urlpatterns = [
    path("rentmachine/", RentMachine.as_view()),
]
