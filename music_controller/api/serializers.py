'''
this module takes a python model (db object)  and return a json object so that we can pass it to the front end
'''

from rest_framework import serializers
from .models import Room

# this class takes a 'Room' class/object and returns a json object with the specified 'fields' using the Modelserializer (inherited)


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ('id', 'code', 'host', 'guest_can_pause',
                  'votes_to_skip', 'created_at')
