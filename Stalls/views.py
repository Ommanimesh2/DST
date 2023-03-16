from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from rest_framework import status, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, AllowAny
from .models import Stalls
from .serializer import StallsSerializer
from rest_framework.request import Request


class AddStalls(ListAPIView):
    serializer_class= StallsSerializer
    permission_classes=[]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['id', 'Stallstopic']
    search_fields = ['Stallstopic']
    def post(self , request : Request):
        serializer = StallsSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save() 
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
       
    def get_queryset(self):
        queryset = Stalls.objects.all()
        return queryset
    
class UpdateStalls(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_object(self,pk):
        try:
            return Stalls.objects.get(pk=pk)
        
        except Stalls.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)
    
    def get(self,request,pk):
        List = self.get_object(pk)
        serializer = StallsSerializer(List)
        return Response(serializer.data)
    
    def put(self, request, pk):
        List = self.get_object(pk)
        serializer = StallsSerializer(List, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        List = self.get_object(pk)
        List.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
