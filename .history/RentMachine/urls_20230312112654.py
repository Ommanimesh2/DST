from django.contrib import admin
from django.urls import path
from .views import 

urlpatterns = [
    path("rentmachine/", JobView.as_view()),
]
