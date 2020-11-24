from django.contrib import admin
from .models import Foodtruck

@admin.register(Foodtruck)
class foodtruckAdmin(admin.ModelAdmin):
  list_display = ['name', 'address', 'longitude', 'latitude', 'menu', 'isOpen']
