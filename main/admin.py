from django.contrib import admin
from .models import Treatment, Doctor, Client, Service


admin.site.register(Treatment)
admin.site.register(Doctor)
admin.site.register(Client)
admin.site.register(Service)