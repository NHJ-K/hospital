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

    #path('login/', views.login, name='login'),
    #path('log/', views.log, name='log'),
    re_path(r'^login/$', views.CustomLogin.as_view(template_name= 'login.html'), name='login'),
    re_path(r'^logout/$', auth_views.LogoutView.as_view(template_name= 'logout.html'), name='logout'),
    re_path(r'^signup/$', core_views.signup, name='signup'),

    re_path(r'^doctor/entry/$', core_views.AddDoctorView, name='doctor-entry'),
    re_path(r'^doctor/appointment/$', core_views.AddAppointment, name='appointment'),
    path('appointment/<int:pk>/delete/', views.AppointmentDelete.as_view(), name='delete-appointment'),
    re_path(r'^list/$', views.DocListView.as_view(), name='list'),
    path('cardio',views.cardio,name='cardio'),
    path('dentist',views.dentist,name='dentist'),
    path('neuro',views.neuro,name='neuro'),
    path('gyno',views.gyno,name='gyno'),
    path('nephro',views.nephro,name='nephro'),
    path('pulmono',views.pulmono,name='pulmono'),
    re_path(r'^profile/$', views.AppointmentListView.as_view(), name='profile'),
    path('doctor/<int:pk>/', views.DocDetailView.as_view(), name='doctor'),
    #re_path(r'^feedback/$', views.feedback_form,name='home'),
    path('appoinment',views.appo,name='appoinment'),
    path('telemed',views.telemed,name='telemed'),
    path('labreport',views.labreport,name='labreport'),
    path('vlabre',views.vlabreport,name='vlabre'),

]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)