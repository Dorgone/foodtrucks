from django.db import models

class Foodtruck(models.Model):
    name = models.CharField(max_length=200) # called 'applicant' in DataSF JSON file
    address = models.CharField(max_length=500)
    longitude = models.DecimalField(max_digits=22, decimal_places=16, blank=True, null=True)
    latitude = models.DecimalField(max_digits=22, decimal_places=16, blank=True, null=True)
    menu = models.TextField(blank=True, null=True) # called 'fooditems' in DataSF JSON file
    isOpen = models.BooleanField(default=False) # used to open or close a food truck popup info window on the map in the frontend 

    class Meta:
        unique_together = (('name', 'address'),) # ensures that there is only one food truck with a given (name, address) tuple