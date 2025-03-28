from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='penplus_home'),
    path('dashboard/', views.dashboard, name='penplus_dashboard'),
]
