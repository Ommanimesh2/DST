from django.contrib import admin
from django.urls import path
from .views import RentMachine,UpdateRent,UserRent,Orderss,Query,FourImg,KVK,KVK_pk


urlpatterns = [
  path("rentmachine/", RentMachine.as_view()),
  path("rentdata/<int:pk>", UpdateRent.as_view()),
 path("rentdatauser/<int:pk>", UserRent.as_view()), 
 path("rentinfo/", Orderss.as_view()),
 path("query/", Query.as_view()),
 path("imgs/", FourImg.as_view()),
 path("kvks/", KVK.as_view()),
 path("kvk/<int:pk>", KVK_pk.as_view())
]
