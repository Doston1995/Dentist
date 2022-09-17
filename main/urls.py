from django.urls import path
from .views import home, doctors, clients, addClient, addDoctor, addRegistration, addTreatment, treatments

urlpatterns = [
    path('', home, name = 'homepage'),
    path('addRegistration', addRegistration, name = 'addRegistration'),
    path('doctors/', doctors, name = 'doctors'),
    path('adddoctor/', addDoctor, name = 'doctorAddForm'),
    path('clients/', clients, name = 'clients'),
    path('addclient/', addClient, name = 'addClient'),
    path('treatments/', treatments, name = 'treatments'),
    path('addTreatment/', addTreatment, name = 'addTreatment'),
]
