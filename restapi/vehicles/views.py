from django.shortcuts import render
from vehicles.models import Vehicle
from vehicles.serializers import VehiclesSerializer
from rest_framework import viewsets


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Vehicles to be viewed or edited.
    """
    queryset = Vehicle.objects.all()
    serializer_class = VehiclesSerializer
    #permission_classes = [permissions.IsAuthenticated]