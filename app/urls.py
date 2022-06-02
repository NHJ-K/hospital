from django.urls import path,re_path
from django.conf import settings
from django.conf.urls.static import static
#from django.conf.urls import url
from    .import views as core_views
from    .import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('payment', views.PaymentPageView.as_view(), name='payment'),
    path('payment_confirm/', views.PaymentConfirmPageView.as_view(), name='payment_confirm'),

    re_path(r'^login/$', auth_views.LoginView.as_view(template_name= 'login.html'), name='login'),
    re_path(r'^logout/$', auth_views.LogoutView.as_view(template_name= 'logout.html'), name='logout'),
    re_path(r'^signup/$', core_views.signup, name='signup'),

    re_path(r'^doctor/entry/$', core_views.AddDoctorView, name='doctor-entry'),
    re_path(r'^doctor/appointment/$', core_views.AddAppointment, name='appointment'),
    path('appointment/<int:pk>/delete/', views.AppointmentDelete.as_view(), name='delete-appointment'),
    re_path(r'^list/$', views.DocListView.as_view(), name='list'),
    re_path(r'^profile/$', views.AppointmentListView.as_view(), name='profile'),
    path('doctor/<int:pk>/', views.DocDetailView.as_view(), name='doctor'),

]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
