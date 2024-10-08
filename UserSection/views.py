from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from .models import Vehicle, Passenger, Driver
from django.views.decorators.csrf import ensure_csrf_cookie
import random
from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import SignUpForm, LoginForm
from .models import CustomUser
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from .models import Comment
from .forms import CommentForm
from django.contrib.auth.mixins import LoginRequiredMixin
from .observers import notify_admin_new_comment


class SignUpView(View):
    form_class = SignUpForm
    template_name = 'signup.html'

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user_data = form.cleaned_data
            user = CustomUser()
            user.save_user(user_data)
            login(request, user)
            return redirect('dashboard')
        return render(request, self.template_name, {'form': form})


'''def signupAccount(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user_data = form.cleaned_data
            user_type = 'custom'  # Hardcoded for now, but can be dynamic.

            # Use the UserFactory to create the user
            user = UserFactory.create_user(user_type, user_data)

            # Log in the newly created user
            login(request, user)

            return render(request, 'dashboard.html')
    else:
        form = SignUpForm()

    return render(request, 'signup.html', {'form': form})


def signupAccount(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            # Obtén los datos limpios del formulario
            user_data = form.cleaned_data

            # Inyectamos la abstracción, en este caso, CustomUser que implementa AbstractUser
            user: AbstractUser = CustomUser()

            # Guardamos el usuario a través de la abstracción
            user.save_user(user_data)

            # Iniciamos sesión para el usuario recién creado
            login(request, user)

            return render(request, 'dashboard.html')
    else:
        form = SignUpForm()

    return render(request, 'signup.html', {'form': form})'''


@login_required
def logoutAccount(request):
    logout(request)
    return render(request, 'index.html')


@ensure_csrf_cookie
def loginAccount(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')  # Redirige al dashboard si el login es exitoso
            else:
                # Usuario no autenticado
                return render(request, 'login.html', {'form': form, 'error': 'Invalid credentials'})
        else:
            return render(request, 'login.html', {'form': form, 'error': 'Form is not valid'})
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


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


class CommentListView(ListView):
    model = Comment
    template_name = 'comments/comment_list.html'
    context_object_name = 'comments'
    ordering = ['-created_at']


class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'comments/add_comment.html'
    success_url = reverse_lazy('comment_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        response = super().form_valid(form)

        # Notificar cuando se agregue un nuevo comentario (Observer)
        notify_admin_new_comment(self.object)
        return response

