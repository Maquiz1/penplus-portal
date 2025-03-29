from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='pedx_home'),
    path('dashboard/', views.dashboard, name='pedx_dashboard'),
]
