from django.http.response import HttpResponse
from django.shortcuts import render
from rest_framework import generics, serializers
from .serializers import RoomSerializer
from .models import Room

# Create your views here.

'''
 we can have both functions and classes fuctioning as views
'''


class RoomView(generics.CreateAPIView):
    # we need to provide the 2 following objects for this view - queryset & serializer_class
    queryset = Room.objects.all()  # what do we want to return
    serializer_class = RoomSerializer  # convert to json object
