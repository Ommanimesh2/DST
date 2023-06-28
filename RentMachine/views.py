from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from rest_framework import status, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, AllowAny
from .models import Renting,Orders,query,FourImages,KVKs
from .serializer import RentingSerializer,OrderSerializer,QuerySerializer,FourImgSerializer,KVKSerializer
from rest_framework.request import Request
from rest_framework.authentication import TokenAuthentication
from rest_framework.views import APIView
from rest_framework.decorators import api_view,authentication_classes,permission_classes
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.pagination import PageNumberPagination
from django.core import serializers
from django.http import JsonResponse
from django.db.models import F


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 8
    page_size_query_param = 'page_size'
    max_page_size = 1000

class KVK(ListAPIView):
    serializer_class=KVKSerializer
    permission_classes=[]

    def post(self , request : Request):
        serializer = KVKSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save() 
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
       
    def get_queryset(self):
        queryset = KVKs.objects.all().order_by('Name_KVK')
        return queryset

class KVK_pk(ListAPIView):
    def get_object(self,pk):
        try:
            return KVKs.objects.get(pk=pk)
        
        except KVKs.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)
    

    def get(self,request,pk):
        List = self.get_object(pk)
        serializer = KVKSerializer(List)
        return Response(serializer.data)
    
    def put(self, request, pk):
        List = self.get_object(pk)
        serializer = KVKSerializer(List, data=request.data)
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
        serializer = KVKSerializer(List, data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        return Response(code=400, data="wrong parameters")



class RentMachine(ListAPIView):
    serializer_class= RentingSerializer
    permission_classes=[]
    pagination_class = StandardResultsSetPagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter , filters.OrderingFilter]
    filterset_fields = ['id', 'Name']
    ordering_fields = [ 'Product', 'quantity']
    search_fields = ['^Name','^KVK__Name_KVK']
    def post(self, request):
        data = request.data  
        serializer = RentingSerializer(data=data)
        if not serializer.is_valid():
            return JsonResponse(serializer.errors, status=400)
        
        kvk_id = data.get('KVK')
        try:
            kvk = KVKs.objects.get(id=kvk_id)
        except KVKs.DoesNotExist:
            return JsonResponse({'error': 'Invalid KVK ID'}, status=400)
        
        renting = Renting.objects.create(
            KVK=kvk,
            Name=data.get('Name'),
            MachineDetails=data.get('MachineDetails'),
            Price=data.get('Price'),
            Contact=data.get('Contact'),
            date=data.get('date')
        )
        response_data = RentingSerializer(renting).data
        
        return JsonResponse(response_data, status=201)
       
    def get_queryset(self):
       queryset = Renting.objects.all()  
       return queryset 



class UpdateRent(APIView):
    pagination_class = StandardResultsSetPagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter , filters.OrderingFilter]
    filterset_fields = ['KVK', 'Name']
    ordering_fields = [ 'Product', 'quantity']
    search_fields = ['^Name']
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

    def get_object(self,pk,**kwargs):
        user_id = kwargs['pk']
        try:
            return Renting.objects.get( pk==user_id)
        
        except Renting.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)
    
     

    def get(self,request,pk):
        List = self.get_object(pk)
        serializer = RentingSerializer(List)
        return Response(serializer.data)


class Orderss(ListAPIView):
    serializer_class= OrderSerializer
    permission_classes=[]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    def post(self , request : Request):
        serializer = OrderSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save() 
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
       
    def get_queryset(self):
        queryset = Orders.objects.all()
        return queryset
    

class Query(ListAPIView):
    serializer_class= QuerySerializer
    permission_classes=[]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    
    def post(self , request : Request):
        serializer = QuerySerializer(data=request.data)

        if serializer.is_valid():
            serializer.save() 
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
       
    def get_queryset(self):
        queryset = query.objects.all()
        return queryset


class FourImg(ListAPIView):
    serializer_class= FourImgSerializer
    permission_classes=[]   
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    def post(self , request : Request):
        serializer = FourImgSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save() 
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
       
    def get_queryset(self):
        queryset = FourImages.objects.all()
        return queryset