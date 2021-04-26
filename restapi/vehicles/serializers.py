from rest_framework import serializers
from vehicles.models import Vehicle

class VehiclesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = ['id','model', 'brand', 'price', 'note']