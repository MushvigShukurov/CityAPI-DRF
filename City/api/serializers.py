from rest_framework import serializers
from City.models import City

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City 
        fields = ['id','name','image','created_at','updated_at']