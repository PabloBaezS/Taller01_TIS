from django.shortcuts import render, redirect
from .forms import RouteForm
from .models import Route
import os
from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render
from gmplot import gmplot
from UserSection.models import Passenger
import polyline as polyline
import requests
from gmplot import gmplot


def driver_view(request):
    if request.method == 'POST':
        origin = request.POST.get('origin')
        destination = request.POST.get('destination')

        # Define the API endpoint for the Directions API
        endpoint = "https://maps.googleapis.com/maps/api/directions/json"

        # Set your Google Maps API key
        key = "AIzaSyBaJ_KORpCWjJT8tP4N7L6VSRoHPHUTXFg"

        # Define the API parameters
        params = {
            "origin": origin,
            "destination": destination,
            "key": "AIzaSyBaJ_KORpCWjJT8tP4N7L6VSRoHPHUTXFg"  # Replace with your own API key
        }

        # Send the API request
        response = requests.get(endpoint, params=params).json()

        # Extract the encoded polyline from the first route if available, otherwise set it to an empty string
        encoded_polyline = response["routes"][0]["overview_polyline"]["points"] if "routes" in response and len(response["routes"]) > 0 else ""

        # Decode the polyline into a list of coordinates
        route_points = polyline.decode(encoded_polyline)

        # Create the plot object
        gmap = gmplot.GoogleMapPlotter(6.244203, -75.581211, 12)

        for lats, lngs in route_points:
            gmap.marker(lats, lngs)

        # Plot the route on the map
        lats, lngs = zip(*route_points)
        print(route_points)
        gmap.plot(lats, lngs, 'cornflowerblue', edge_width=10)

        # Save the map to an HTML file
        gmap.draw("static/route.html")

        return render(request, 'driverView.html')

    return render(request, 'driverView.html')

def passenger_view(request):
    if request.method == 'POST':
        location = request.POST.get('location')

        # Here you can process and save the location as needed
        # For example, you can save it to a database or perform other operations

        # Render a success page or redirect to another view
        return render(request, 'success.html')

    # Render the form page if it's a GET request
    return render(request, 'passengerView.html')


def save_route(request):
    if request.method == 'POST':
        form = RouteForm(request.POST)
        if form.is_valid():
            origin = form.cleaned_data['origin']
            destination = form.cleaned_data['destination']

            # Define the API endpoint for the Directions API
            endpoint = "https://maps.googleapis.com/maps/api/directions/json"

            # Define the API parameters
            params = {
                "origin": origin,
                "destination": destination,
                "key": "AIzaSyBaJ_KORpCWjJT8tP4N7L6VSRoHPHUTXFg"  # Replace with your own API key
            }

            # Send the API request
            response = requests.get(endpoint, params=params).json()

            # Extract the encoded polyline from the response
            encoded_polyline = response["routes"][0]["overview_polyline"]["points"]

            # Decode the polyline into a list of coordinates
            route_points = polyline.decode(encoded_polyline)

            # Create the plot object
            gmap = gmplot.GoogleMapPlotter(0, 0, 2)

            for lats, lngs in route_points:
                gmap.marker(lats, lngs)

            # Plot the route on the map
            lats, lngs = zip(*route_points)
            print(route_points)
            route = Route.objects.create(origin=origin, destination=destination, route_points=encoded_polyline)
            route.save()

            return render(request, 'driverView.html')  # Replace 'dashboard' with the URL name for the dashboard page
    else:
        form = RouteForm()

    return render(request, 'driverView.html', {'form': form})




def save_location(request):
    if request.method == 'POST':
        location = request.POST.get('location')
        passenger = Passenger.objects.get(id=request.user.id)
        passenger.location = location
        passenger.save()

    return redirect('passenger_view')

