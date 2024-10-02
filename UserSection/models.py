from django.conf import settings
from django.contrib.auth.models import AbstractUser as DjangoAbstractUser
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.db import models
from django.core.validators import EmailValidator


# Clase para usuario que extiende el usuario de Django
class CustomUser(DjangoAbstractUser):
    phone = models.CharField(max_length=20)
    address = models.ForeignKey('Address', on_delete=models.SET_NULL, null=True,
                                blank=True)

    def save_user(self, user_data):
        self.username = user_data.get('username')
        self.email = user_data.get('email')
        self.save()


# Modelo Address para normalizar la dirección
class Address(models.Model):
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.street}, {self.city}"


# Clase concreta para vehículo
class Vehicle(models.Model):
    license_plate = models.CharField(max_length=10)

    def save_vehicle(self, vehicle_data):
        self.license_plate = vehicle_data.get('license_plate')
        self.save()


# Definición de Driver, Passenger y Admin después de CustomUser
class Driver(CustomUser):
    driverLicense = models.CharField(max_length=50)
    car = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    rate = models.FloatField()


class Passenger(CustomUser):
    location = models.CharField(max_length=100, default=None)


class Admin(CustomUser):
    account = models.CharField(max_length=100)
    customuser_ptr = models.OneToOneField(CustomUser, on_delete=models.CASCADE,
                                          parent_link=True, primary_key=True)


# Comentarios y notificaciones
class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.user.username} at {self.created_at}'


# UserFactory para crear diferentes tipos de usuarios
class UserFactory:
    @staticmethod
    def create_user(user_type, user_data):
        if user_type == 'custom':
            user = CustomUser()
        elif user_type == 'driver':
            user = Driver()
        elif user_type == 'passenger':
            user = Passenger()
        else:
            raise ValueError(f"Unknown user type: {user_type}")

        user.save_user(user_data)
        return user
