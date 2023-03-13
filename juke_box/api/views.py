from django.shortcuts import render
from rest_framework import generics
from .models import Room
from .serialziers import RoomSerializer

# Create your views here.

'''View and create different rooms'''
class RoomView(generics.ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer