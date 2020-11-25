from rest_framework import generics, mixins
from foodtrucks.models import Foodtruck
from .serializers import foodtruckSerializer
import requests

class foodtruckAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    resource_name = "foodtrucks"
    serializer_class = foodtruckSerializer
    pagination_class = None # removes pagination so the API supplies all of the food trucks at once

    def initialize_dataset(self): # populates database with foodtrucks data from SF government API

      # downloads foodtrucks JSON file from SF government API
      url = "https://data.sfgov.org/resource/rqzj-sfat.json"
      response = requests.get(url) 
      data = response.json()
      
      # parses JSON file and creates foodtrucks objects in database
      for foodtruck in data:
        # checks if fooditems exists and replaces ":" with ","
        if "fooditems" in foodtruck:
          fooditems = foodtruck["fooditems"]
          fooditems = fooditems.replace(":", ",")
        else:
          fooditems = ""

        # converts longitude and latitude strings
        longitude = float(foodtruck["longitude"])
        latitude = float(foodtruck["latitude"])

        # checks if a foodtruck with this name and address already exists
        # if it does exist, we do nothing
        # if it doesn't, we create one and save it to the database
        obj, created = Foodtruck.objects.get_or_create(
            name=foodtruck["applicant"],
            address=foodtruck["address"],
            defaults={
              'longitude': longitude,
              'latitude': latitude,
              'menu': fooditems,
              'isOpen': False,
            },
        )

        # prints name and address of the foodtruck if it is new to database
        if created:
          print(foodtruck["applicant"], " - ", foodtruck["address"]) 


    def get_queryset(self):
      self.initialize_dataset() # populates database with foodtrucks data from SF government API
      return Foodtruck.objects.all()


    def post(self, request, *args, **kwargs):
      return self.create(request, *args, **kwargs)