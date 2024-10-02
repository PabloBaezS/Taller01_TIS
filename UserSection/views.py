from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import SignUpForm
from django.shortcuts import render, redirect
from .models import Vehicle, CustomUser, Passenger, Driver
from django.views.decorators.csrf import ensure_csrf_cookie
import random



def signupAccount(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            user = form.save()
            login(request, user)
            return render(request,'dashboard.html')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


@login_required
def logoutAccount(request):
    logout(request)
    return render(request, 'index.html')


@ensure_csrf_cookie
def loginAccount(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # Authentication successful, log the user in
            login(request, user)
            return render(request, 'dashboard.html')  # Replace 'dashboard' with the URL name for the dashboard page
        else:
            # Authentication failed, show an error message
            error_message = "Invalid username or password."
            return render(request, 'login.html', {'error_message': error_message})
    else:
        return render(request, 'login.html')


def index(request):
    return render(request, 'index.html')

def security(request):
    return render(request, 'security.html')

def PoolMate(request):
    return render(request, 'PoolMate.html')

def dashboard(request):
    if not request.user.is_authenticated:
        return render(request,'login.html')
    else:
        user = request.user
        context = {
            'user': user
        }
        return render(request, 'dashboard.html', context)


@login_required
def dashboard(request):
    user = request.user
    context = {
        'user': user
    }
    return render(request, 'dashboard.html', context)

@login_required
def passenger_dashboard(request):
    if not request.user.is_passenger:
        return redirect('dashboard.html')  # Redirect to normal dashboard

    user = request.user
    passenger = Passenger.objects.get(id=user.id)
    location = passenger.location

    context = {
        'user': user,
        'location': location
    }

    return render(request, 'passenger_dashboard.html', context)


@login_required
def driver_dashboard(request):
    if not request.user.is_driver:
        return redirect('dashboard')  # Redirect to normal dashboard
    user = request.user
    context = {
        'user': user
    }
    return render(request, 'driver_dashboard.html', context)


def driver_vehicle_info(request):
    message = None
    user = request.user

    if request.method == 'POST':
        model = request.POST.get('model')
        license_plate = request.POST.get('licensePlate')
        color = request.POST.get('color')
        driver_id = random.randint(0,999)
        capacity = request.POST.get('capacity')

        # Save the vehicle information to the database
        vehicle = Vehicle.objects.create(
            model=model,
            licensePlate=license_plate,
            color=color,
            driverId=driver_id,
            capacity=capacity
        )

        message = "Vehicle information saved successfully!"

    return render(request, 'vehicle.html', {'message': message})