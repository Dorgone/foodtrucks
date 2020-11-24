from django.db import models

class Foodtruck(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=500)
    longitude = models.DecimalField(max_digits=22, decimal_places=16, blank=True, null=True)
    latitude = models.DecimalField(max_digits=22, decimal_places=16, blank=True, null=True)
    menu = models.TextField(blank=True, null=True)
    isOpen = models.BooleanField(default=False)

    class Meta:
        unique_together = (('name', 'address'),)