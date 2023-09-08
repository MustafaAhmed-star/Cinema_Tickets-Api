from rest_framework import serializers
from .models import *

class MovieSerialzers(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields ='__all__'
class ReservationSerialzers(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields ='__all__'
class GuestSerialzers(serializers.ModelSerializer):
    class Meta:
        model = Guest
        fields =['pk','reservation_guest','name','mobile']
class PostSerialzers(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields ='__all__'        