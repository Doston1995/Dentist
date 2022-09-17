from django.db import models

CHOICES = (
        ('E', 'Erkak'),
        ('A', 'Ayol'),
    )

class Treatment(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    price = models.CharField(max_length=10)
    
    def __str__(self):
        return self.name   
    
    
    

class Doctor(models.Model):
    lastname = models.CharField(max_length=100)
    firstname = models.CharField(max_length=100)
    patronym = models.CharField(max_length=100)
    birthday = models.DateField()
    gender = models.CharField(max_length=300, choices = CHOICES)
    phoneNumber = models.CharField(max_length=100)
    image = models.ImageField(upload_to = 'image/doctors/')
    pub_date = models.DateTimeField(auto_now_add = True)
    
    def __str__(self):
        return f"{self.lastname} { self.firstname} "

    class Meta:
        ordering = ('-pub_date',)
    
    
class Client(models.Model):
    lastname = models.CharField(max_length=100)
    firstname = models.CharField(max_length=100)
    patronym = models.CharField(max_length=100)
    birthday = models.DateField()
    gender = models.CharField(max_length=300, choices = CHOICES)
    phoneNumber = models.CharField(max_length=100)
    image = models.ImageField(upload_to = 'image/clients/')
    pub_date = models.DateTimeField(auto_now_add = True)
    
    def __str__(self):
        return f"{self.lastname} { self.firstname} "
    
    class Meta:
        ordering = ('-pub_date',)
    

class Service(models.Model):
    client = models.ForeignKey('Client', on_delete = models.CASCADE)
    doctor = models.ForeignKey('Doctor', on_delete = models.CASCADE)
    trietment = models.ForeignKey('Treatment', on_delete = models.CASCADE)
    date = models.DateField()

    class Meta:     
        ordering = ('-date',)