from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.db import models
from django.core.validators import EmailValidator


from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # Add additional fields here
    phone = models.CharField(max_length=20)
    homeAddress = models.CharField(max_length=200)

    def __str__(self):
        return self.username


class Vehicle(models.Model):
    model = models.CharField(max_length=50)
    licensePlate = models.CharField(max_length=20)
    color = models.CharField(max_length=50)
    driverId = models.CharField(max_length=50)
    capacity = models.IntegerField()


class Driver(CustomUser):
    driverLicense = models.CharField(max_length=50)
    car = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    rate = models.FloatField()


class Passenger(CustomUser):
    location = models.CharField(max_length=100, default=None)


class Admin(CustomUser):
    account = models.CharField(max_length=100)
    customuser_ptr = models.OneToOneField(CustomUser, on_delete=models.CASCADE, parent_link=True, primary_key=True)
