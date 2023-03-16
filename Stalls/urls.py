from django.contrib import admin
from django.urls import path
from .views import AddStalls,UpdateStalls

urlpatterns = [
    path("addstalls/", AddStalls.as_view()),
  path("stallsdata/<int:pk>", UpdateStalls.as_view()),
]
