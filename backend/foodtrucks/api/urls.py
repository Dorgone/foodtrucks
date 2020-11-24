from .views import foodtruckAPIView
from django.conf.urls import url

app_name = 'api-foodtrucks' ## necessary to put namespace="api-foodtrucks" in the include in the main urls.py file

urlpatterns = [
    url('', foodtruckAPIView.as_view(), name='foodtruck-list'),
]
