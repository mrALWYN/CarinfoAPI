from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import CarListing
from .serializers import CarListingSerializer

class CarDetails(APIView):
    def get(self, request, car_id):
        try:
            car = CarListing.objects.get(pk=car_id)
            serializer = CarListingSerializer(car)
            return Response(serializer.data)
        except CarListing.DoesNotExist:
            return Response({"message": "Car not found"}, status=status.HTTP_404_NOT_FOUND)
