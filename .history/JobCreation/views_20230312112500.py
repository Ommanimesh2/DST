from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from rest_framework import status, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, AllowAny
from .models import Jobs
from .serializer import JobCreateSerialize
from rest_framework.request import Request


class JobView(ListAPIView):
    serializer_class= JobCreateSerializer
    permission_classes=[]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['id', 'JobTitle']
    search_fields = ['JobTitle']
    def post(self , request : Request):
        serializer = JobCreateSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save() 
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
       

    def get_queryset(self):
        queryset = Jobs.objects.all()
        return queryset

class UpdateJobView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_object(self,pk):
        try:
            return Jobs.objects.get(pk=pk)
        
        except Jobs.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)
    
    def get(self,request,pk):
        List = self.get_object(pk)
        serializer = JobCreateSerializer(List)
        return Response(serializer.data)
    
    def put(self, request, pk):
        List = self.get_object(pk)
        serializer = JobCreateSerializer(List, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        List = self.get_object(pk)
        List.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
