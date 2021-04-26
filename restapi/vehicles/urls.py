from django.conf.urls import url, include
from rest_framework_nested import routers
from vehicles.views import VehicleViewSet

vehicle = routers.SimpleRouter()
vehicle.register(
    r'vehicle',
    VehicleViewSet,
)

urlpatterns = [
    url(r'^', include(vehicle.urls)),   
]