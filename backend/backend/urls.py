from django.contrib import admin
from django.conf.urls import url, include

urlpatterns = [
    url('admin/', admin.site.urls),
    url('api/foodtrucks/', include('foodtrucks.api.urls', namespace='api-foodtrucks')),
]