from django.contrib import admin

# Register your models here.
from Services.models import Service, Doctor, Appointment

admin.site.register(Service)
admin.site.register(Doctor)
admin.site.register(Appointment)
