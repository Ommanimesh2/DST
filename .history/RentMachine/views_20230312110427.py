from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from rest_framework import status, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, AllowAny
from .models import Jobs
from .serializer import JobCreateSerializer
from rest_framework.request import Request


class RentMachine(ListAPIView)
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