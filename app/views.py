from django.views.generic import TemplateView
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from app.forms import SignUpForm, AddDoctorForm, AppointmentForm
from django.views import generic
from app.models import AddDoctor, Appointment,doclogin
from django.views.generic import DetailView
from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView
from django.contrib.auth.models import Group
from django.contrib.auth.models import User

class HomePageView(TemplateView) :
	template_name = 'index.html'
class PaymentPageView(TemplateView):
    template_name = 'payment.html'
class PaymentConfirmPageView(TemplateView):
    template_name = 'confirmation.html'
class BookPageView(TemplateView):
    template_name = 'app.html'

def login(request):
    return render(request, 'login.html')

def log(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        passw = request.POST.get('password')
        if doclogin.objects.filter(mail=uname).exists():
            if doclogin.objects.filter(mail=uname,password=passw).exists():
                return render(request, 'index.html',{'utype=':'Doctor'})
            else:
                return render(request, 'login.html')

def cardio(request):
    doc = AddDoctor.objects.filter(Specialist_in='Cardiology')
    return render(request,'doctor.html',{'doc_list':doc,'object_list':doc})

def dentist(request):
    doc = AddDoctor.objects.filter(Specialist_in='Dentist')
    return render(request,'doctor.html',{'doc_list':doc,'object_list':doc})

def neuro(request):
    doc = AddDoctor.objects.filter(Specialist_in='Neurology')
    return render(request,'doctor.html',{'doc_list':doc,'object_list':doc})

def gyno(request):
    doc = AddDoctor.objects.filter(Specialist_in='Gynaecology')
    return render(request,'doctor.html',{'doc_list':doc,'object_list':doc})

def nephro(request):
    doc = AddDoctor.objects.filter(Specialist_in='Nephrology')
    return render(request,'doctor.html',{'doc_list':doc,'object_list':doc})

def pulmono(request):
    doc = AddDoctor.objects.filter(Specialist_in='Pulmonology')
    return render(request,'doctor.html',{'doc_list':doc,'object_list':doc})

def appo(request):
    username = ""
    if request.user.is_authenticated:
        username = request.user.username
    fil = Appointment.objects.filter(doctor=username)
    return render(request, 'appointment.html', {'vlaue': fil})

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            User = authenticate(username=username, password=raw_password)
            #login(request, User)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


class DocListView(generic.ListView):
    model = AddDoctor
    context_object_name = 'doc_list'
    template_name = 'doctor.html'

    def get_queryset(self):
        return AddDoctor.objects.order_by('Doctor_Name')

class DocDetailView(DetailView):
    model = AddDoctor
    template_name = 'book.html'

def AddDoctorView(request):
    if request.method == 'POST':
        form = AddDoctorForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            user = User.objects.create_user(username=form.cleaned_data['Mail'],
                                            email=form.cleaned_data['Mail'],
                                            password=form.cleaned_data['Password'])
            user.save()
            group = Group.objects.get(name='doc')
            user.groups.add(group)
            #AddDoctor(Doctor_Name=form.cleaned_data.get('Doctor_Name'),Specialist_in=form.cleaned_data.get('Specialist_in'),Hospital_Name=form.cleaned_data.get('Hospital_Name'),Available_Days=form.cleaned_data.get('Available_Days'),Timings=form.cleaned_data.get('Timings'),Phone_Number=form.cleaned_data.get('Phone_Number'),Mail=form.cleaned_data.get('Mail'),Password=form.cleaned_data.get('Password')).save()
            doclogin(mail=form.cleaned_data.get('Mail'),Doctor_Name=form.cleaned_data.get('Doctor_Name'),Specialization=form.cleaned_data.get('Specialist_in'),password=form.cleaned_data.get('Password')).save()
            return redirect('home')
        else:
            print(form.errors)
    else:
        form = AddDoctorForm()
    return render(request, 'adddoctor.html', {'form': form})

def AddAppointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('payment')
    else:
        form = AppointmentForm()
    return render(request, 'app.html', {'form': form})

class AppointmentListView(generic.ListView):
    model = Appointment
    context_object_name = 'app_list'
    template_name = 'profile.html'

    def get_queryset(self):
        return Appointment.objects.filter(first_name=self.request.user)

class AppointmentDelete(DeleteView):
    model = Appointment
    template_name = 'delete_app.html'
    success_url = reverse_lazy('profile')