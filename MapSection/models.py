from django.db import models
import googlemaps
from django.http import HttpResponse
from django.db.models import JSONField


class Route(models.Model):
    origin = models.CharField(max_length=200)
    destination = models.CharField(max_length=200)
    route_points = models.JSONField(default=list)

    def __str__(self):
        return f"Route from {self.origin} to {self.destination}"




