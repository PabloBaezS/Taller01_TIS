from django import forms

class RouteForm(forms.Form):
    origin = forms.CharField(max_length=100)
    destination = forms.CharField(max_length=100)

