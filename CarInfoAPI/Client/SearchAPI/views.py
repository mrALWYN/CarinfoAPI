# CarSearch/SearchAPI/views.py
from django.shortcuts import render
import requests

def search_car(request):
    if 'car_id' in request.GET:
        car_id = request.GET['car_id']
        # Debug: Print the car ID to ensure it's being retrieved correctly
        print("Car ID:", car_id)
        
        # Make a request to the CarCraze API to get the details of the car
        response = requests.get(f'http://localhost:8000/car/{car_id}/')
        
        # Debug: Print the API response status code
        print("API Response Status Code:", response.status_code)
        
        if response.status_code == 200:
            # Debug: Print the API response content to inspect the data returned
            print("API Response Content:", response.content)
            
            car_details = response.json()
            # Debug: Print the car details to verify they are parsed correctly
            print("Car Details:", car_details)
            
            return render(request, 'car_details.html', {'car_details': car_details})
        else:
            # Debug: Print an error message if the API request fails
            print("Error: Car not found")
            return render(request, 'error.html', {'error': 'Car not found'})
    else:
        return render(request, 'search.html')
