from rest_framework import generics, mixins
from foodtrucks.models import Foodtruck
from .serializers import foodtruckSerializer
import requests

class foodtruckAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    resource_name = "foodtrucks"
    serializer_class = foodtruckSerializer
    pagination_class = None

    def initialize_dataset(self):
      url = "https://data.sfgov.org/resource/rqzj-sfat.json"

      response = requests.get(url)
      data = response.json()
      
      for foodtruck in data:
        if "fooditems" in foodtruck:
          fooditems = foodtruck["fooditems"]
          fooditems = fooditems.replace(":", ",")
        else:
          fooditems = ""
        longitude = float(foodtruck["longitude"])
        latitude = float(foodtruck["latitude"])

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
        if created:
          print(foodtruck["applicant"], " - ", foodtruck["address"])


    def get_queryset(self):
      #Foodtruck.objects.all().delete()
      self.initialize_dataset()
      return Foodtruck.objects.all()


    def post(self, request, *args, **kwargs):
      return self.create(request, *args, **kwargs)