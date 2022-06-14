from django.db import models
from django.urls import reverse

class AddDoctor(models.Model):
    Doctor_Name = models.CharField(max_length=100)
    Specialist_in = models.CharField(max_length=50)
    Hospital_Name = models.CharField(max_length=100)
    Available_Days = models.CharField(max_length=100)
    Timings = models.CharField(max_length=50)
    Phone_Number = models.CharField(max_length=10)
    Mail = models.CharField(max_length=50)
    Password = models.CharField(max_length=50,default="1234")

    def get_absolute_url(self):
        return reverse('doctor', args=[str(self.id)])
    def __str__(self):
        return self.Doctor_Name

class Appointment(models.Model):
    first_name = models.CharField(max_length=50)
    second_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=6)
    age = models.CharField(max_length=2)
    day = models.CharField(max_length=10)
    timing = models.CharField(max_length=10)
    problem = models.CharField(max_length=150)
    symptoms = models.CharField(max_length=150)
    phone = models.CharField(max_length=10)
    mail = models.EmailField(max_length=50)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=30)
    doctor = models.CharField(max_length=50,default="None")

    def get_absolute_url(self):
        return reverse('app', args=[str(self.id)])
    def __str__(self):
        return self.first_name

class doclogin(models.Model):
    mail = models.CharField(max_length=50)
    Doctor_Name = models.CharField(max_length=50)
    Specialization = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    

class Feedback(models.Model):
    customer_name = models.CharField(max_length=120)
    email = models.EmailField()
    details = models.TextField()
    happy = models.BooleanField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.customer_name

class files(models.Model):
    title = models.CharField(max_length=50)
    Doctor_Email = models.CharField(max_length=50)
    #filename = models.CharField(max_length=50)
    file = models.FileField()
