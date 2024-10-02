"""PoolMate URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from UserSection.views import index, loginAccount, signupAccount, logoutAccount, security, PoolMate, dashboard, driver_vehicle_info
from MapSection.views import driver_view, save_route, save_location, passenger_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', signupAccount, name='signup'),
    path('logoutAccount/', logoutAccount, name='logoutAccount'),
    path('login/', loginAccount, name='login'),
    path('', index, name='index'),
    path('driver-view/', driver_view, name='driver_view'),
    path('save-route/', save_route, name='save_route'),
    path('security/', security, name='security'),
    path('PoolMate/', PoolMate, name='PoolMate'),
    path('dashboard', dashboard, name='dashboard'),
    path('passenger-view/', passenger_view, name='passenger_view'),
    path('save-location/', save_location, name='save_location'),
    path('vehicle-info/', driver_vehicle_info, name='driver_vehicle_info'),
]
