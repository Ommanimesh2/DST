from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from rest_framework import status, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, AllowAny
from .models import Renting
from .serializer import RentingSerializer
from rest_framework.request import Request
from rest_framework.authentication import TokenAuthentication
from rest_framework.views import APIView
from rest_framework.decorators import api_view,authentication_classes,permission_classes
from rest_framework.authentication import SessionAuthentication, BasicAuthentication


class RentMachine(ListAPIView):
    serializer_class= RentingSerializer
    permission_classes=[]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['id', 'Name']
    search_fields = ['Name']
    def post(self , request : Request):
        serializer = RentingSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save() 
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
       
    def get_queryset(self):
        queryset = Renting.objects.all()
        return queryset
    
   

class UpdateRent(APIView):
    @authentication_classes((SessionAuthentication, TokenAuthentication, BasicAuthentication))
    @permission_classes((IsAuthenticated,))


    def get_object(self,pk):
        try:
            return Renting.objects.get(pk=pk)
        
        except Renting.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)
    
     

    def get(self,request,pk):
        List = self.get_object(pk)
        serializer = RentingSerializer(List)
        return Response(serializer.data)
    
    def put(self, request, pk):
        List = self.get_object(pk)
        serializer = RentingSerializer(List, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        List = self.get_object(pk)
        List.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

    def patch(self, request ,pk):
        List = self.get_object(pk)
        data=request.data
        serializer = RentingSerializer(List, data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        return Response(code=400, data="wrong parameters")
    

class UserRent(APIView):

    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['user_id', 'Name']
    search_fields = ['user_id']

    @authentication_classes((SessionAuthentication, TokenAuthentication, BasicAuthentication))
    @permission_classes((IsAuthenticated,)) 

    # def get_object(self,pk):
        
    #     try:
    #         return Renting.objects.get(pk='user_id')
        
    #     except Renting.DoesNotExist:
    #         return HttpResponse(status=status.HTTP_404_NOT_FOUND)
    
     

    def get_queryset(self, request, *args, pk):
        queryset = Renting.objects.get(pk=self.kwargs['id'])
        return queryset


