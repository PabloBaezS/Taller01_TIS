from django.contrib import admin
from UserSection.models import CustomUser, Vehicle, Driver, Passenger, Admin

admin.site.register(CustomUser)
admin.site.register(Vehicle)
admin.site.register(Driver)
admin.site.register(Passenger)
admin.site.register(Admin)

