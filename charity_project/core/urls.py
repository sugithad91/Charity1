# core/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('causes/', views.causes, name='causes'),
    path('donate/', views.donate, name='donate'),
    path('contact/', views.contact, name='contact'),
    path('donation-success/', views.thank_you, name='donation_success'),
    path('volunteer/', views.volunteer_view, name='volunteer'),



]
