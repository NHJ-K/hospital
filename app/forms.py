from django import forms
from app import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from app.models import AddDoctor, Appointment,doclogin
from material import *

class SignUpForm(UserCreationForm):
    username = forms.CharField()
    first_name = forms.CharField(required=False)
    last_name = forms.CharField(required=False)
    email = forms.EmailField(label="Email Address")
    password1 = forms.CharField(widget=forms.PasswordInput, label="Enter password")
    password2 = forms.CharField(widget=forms.PasswordInput, label="Confirm password")
    receive_news = forms.BooleanField(required=False, label='I want to receive news and notifications')
    agree_toc = forms.BooleanField(required=True, label='I agree with the Terms and Conditions')

    layout = Layout('username', 'email',
                    Row('password1', 'password2'),
                    Fieldset('Pesonal details',
                             Row('first_name', 'last_name'),
                              'receive_news', 'agree_toc'))
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2',)


class AppointmentForm(forms.ModelForm):
    first_name = forms.CharField(label="Username")
    second_name = forms.CharField()
    mail = forms.EmailField()
    phone = forms.CharField()
    gender = forms.ChoiceField(choices=(('M', 'Male'), ('F', 'Female'), ('O', 'Other')), widget=forms.RadioSelect)
    age = forms.IntegerField()
    day = forms.CharField(label="Preferred Day")
    address = forms.CharField()
    timing = forms.CharField(label="Preferred Timings")
    problem = forms.CharField()
    symptoms = forms.CharField()
    city = forms.CharField()
    doctor = forms.CharField(label="Doctor Email")

    layout = Layout(
        Row('first_name', 'second_name'),
        Row('mail', 'phone'),
        Row('age', 'city'),
        'address',
        'problem',
        'symptoms',
        Fieldset('Contact Details',
                 Row(Column('gender', span_columns=4),
                     Column('day',
                            Row('timing'),
                            Row('doctor'),
                            span_columns=8))))

    class Meta:
        model = Appointment
        fields = ('first_name', 'second_name', 'gender', 'age', 'day', 'timing', 'problem'
                  , 'symptoms', 'phone', 'mail', 'address', 'city','doctor')

class AddDoctorForm(forms.ModelForm):
    Doctor_Name = forms.CharField()
    Specialist_in = forms.CharField()
    Hospital_Name = forms.CharField()
    Available_Days = forms.CharField(label="Ex: Mon - Fri")
    Timings = forms.CharField(label="Ex: 10AM - 4PM")
    Phone_Number = forms.CharField()
    Mail = forms.CharField()
    Password = forms.CharField(widget=forms.PasswordInput)


    layout = Layout(Fieldset('Doctor details',
                            Row('Doctor_Name',),
                            Row('Specialist_in', 'Hospital_Name'),
                            Row('Available_Days', 'Timings'),
                            Fieldset('Contact details',
                                    Row('Phone_Number', 'Mail'),
                                    Row('Password'))))
    class Meta:
        model = AddDoctor
        fields = ('Doctor_Name', 'Specialist_in', 'Hospital_Name', 'Available_Days', 'Timings', 'Phone_Number', 'Mail', 'Password')
    
