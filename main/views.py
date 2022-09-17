from django.shortcuts import render, redirect
from .models import Treatment, Doctor, Client, Service
from .forms import DoctorForm, ClientForm, TreatmentForm, ServiceForm
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def home(request):
    if request.method =='POST':
        query = request.POST.get('q')
        services = Service.objects.filter(Q(client__lastname__icontains=query) | Q(client__firstname__icontains=query) |
                                            Q(client__patronym__icontains=query) | Q(doctor__lastname__icontains=query) |
                                            Q(doctor__patronym__icontains=query) | Q(trietment__name__icontains=query) |
                                            Q(date__icontains=query))   
    else:
        services = Service.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(services, 1)
    try:
        services = paginator.page(page)
    except PageNotAnInteger:
        services = paginator.page(1)
    except EmptyPage:
        services = paginator.page(paginator.num_pages)
    context = {
    'services':services
        }
    return render(request, 'registrations.html', context)   


def addRegistration(request):
    if request.method =='POST':
        form = ServiceForm(request.POST)
        if form.is_valid():
            register = form.save(commit = False)
            register.save()
            return redirect(home)
        else:
            return render(request, 'addRegistration.html', {'form':form})
    else:
        form = ServiceForm(None)  
        return render(request, 'addRegistration.html', {'form':form})


def doctors(request):
    if request.method =='POST': 
        query = request.POST.get('q') 
        doctors = Doctor.objects.filter(Q(lastname__icontains=query) | Q(firstname__icontains=query) |
                                            Q(patronym__icontains=query) | Q(birthday__icontains=query) |
                                            Q(phoneNumber__icontains=query))
    else:
        doctors = Doctor.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(doctors, 1)
    try:
        doctors = paginator.page(page)
    except PageNotAnInteger:
        doctors = paginator.page(1)
    except EmptyPage:
        doctors = paginator.page(paginator.num_pages)
    context = {
        'doctors':doctors
         }
    return render(request, 'doctors.html', context)


def addDoctor(request):
    if request.method =='POST': 
        form = DoctorForm(request.POST, request.FILES)
        if form.is_valid():
            doctor = form.save(commit = False)
            doctor.save() 
            return redirect(doctors)
        else:
            return render(request, 'addDoctor.html', {'form':form})
    else:
        form = DoctorForm(None)  
        return render(request, 'addDoctor.html', {'form':form})


def clients(request):
    if request.method =='POST': 
        query = request.POST.get('q') 
        clients = Client.objects.filter(Q(lastname__icontains=query) | Q(firstname__icontains=query) |
                                        Q(patronym__icontains=query) | Q(birthday__icontains=query) |
                                        Q(phoneNumber__icontains=query))
    else:   
        clients = Client.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(clients, 1)
    try:
        clients = paginator.page(page)
    except PageNotAnInteger:
        clients = paginator.page(1)
    except EmptyPage:
        clients = paginator.page(paginator.num_pages)
    context = {
            'clients':clients
        }
    return render(request, 'clients.html', context)


def addClient(request):
    if request.method =='POST': 
        form = ClientForm(request.POST, request.FILES)
        if form.is_valid():
            client = form.save(commit = False)
            client.save() 
            return redirect(clients)
        else:
            return render(request, 'addClient.html', {'form':form})
    else:
        form = ClientForm(None)  
        return render(request, 'addClient.html', {'form':form})


def treatments(request):
    if request.method =='POST': 
        query = request.POST.get('q') 
        treatments   = Treatment.objects.filter(Q(name__icontains=query) | Q(price__icontains=query))
    else:       
        treatments = Treatment.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(treatments, 1)
    try:
        treatments = paginator.page(page)
    except PageNotAnInteger:
        treatments = paginator.page(1)
    except EmptyPage:
        treatments = paginator.page(paginator.num_pages)
    context = {
            'treatments':treatments}
    return render(request, 'treatments.html', context)


def addTreatment(request):
    if request.method =='POST': 
        form = TreatmentForm(request.POST)
        if form.is_valid():
            treatment = form.save(commit = False)
            treatment.save() 
            return redirect(treatments)
        else:
            return render(request, 'addTreatment.html', {'form':form})
    else:
        form = TreatmentForm(None)  
        return render(request, 'addTreatment.html', {'form':form})



