from rest_framework import serializers
from foodtrucks.models import Foodtruck

class foodtruckSerializer(serializers.ModelSerializer):
    class Meta:
        model = Foodtruck
        fields = (
            "id",
            "name", 
            "address", 
            "longitude",
            "latitude",
            "menu",
            "isOpen",
        )