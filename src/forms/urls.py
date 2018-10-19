from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('rsvpform/', views.rsvpform, name='rsvpform'),
]
