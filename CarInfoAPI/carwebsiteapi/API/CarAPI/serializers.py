from rest_framework import serializers
from .models import CarListing

class CarListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarListing
        fields = ['name', 'model', 'year', 'mileage', 'price', 'description', 'features']
