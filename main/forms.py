from django.forms import ModelForm
from django import forms
from .models import Client, Doctor, Service, Treatment


class DateInput(forms.DateInput):
    input_type = 'date'

class TreatmentForm(ModelForm):
    class Meta:
        model = Treatment       
        fields =["name", "price", "description" ]
        
    def __init__(self, *args, **kwargs):
        super(TreatmentForm, self).__init__(*args, **kwargs)
        
        self.fields['name'].widget.attrs['placeholder'] = 'Muolaja nomi'
        self.fields['price'].widget.attrs['placeholder'] = 'Muolaja narxi'
        
class ClientForm(ModelForm):
    birthday = forms.DateField(widget = DateInput(format="%d-%m%-Y"))
    class Meta:
        model = Client       
        fields =["lastname", "firstname", "patronym","birthday", "gender", "phoneNumber","image" ]
        
    def __init__(self, *args, **kwargs):
        super(ClientForm, self).__init__(*args, **kwargs)
        
        self.fields['lastname'].widget.attrs['placeholder'] = 'Familiyasi'
        self.fields['firstname'].widget.attrs['placeholder'] = 'Ismi'
        self.fields['patronym'].widget.attrs['placeholder'] = 'Otasining ismi'
        self.fields['phoneNumber'].widget.attrs['placeholder'] = 'Telefon raqami'
        

class DoctorForm(ModelForm):
    birthday = forms.DateField(widget = DateInput(format="%d-%m%-Y"))
    class Meta:
        model = Doctor       
        fields =["lastname", "firstname", "patronym", "birthday", "gender" , "phoneNumber","image"]
    
    def __init__(self, *args, **kwargs):    
        super(DoctorForm, self).__init__(*args, **kwargs)
        
        self.fields['lastname'].widget.attrs['placeholder'] = 'Familiyasi'
        self.fields['firstname'].widget.attrs['placeholder'] = 'Ismi'
        self.fields['patronym'].widget.attrs['placeholder'] = 'Otasining ismi'
        self.fields['phoneNumber'].widget.attrs['placeholder'] = 'Telefon raqami'


class ServiceForm(ModelForm):
    date = forms.DateField(widget = DateInput(format="%d-%m%-Y"))
    class Meta:
        model = Service       
        fields =["client", "doctor", "trietment", "date"]