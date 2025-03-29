from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='logbook_home'),
    path('records/', views.records, name='logbook_records'),
]
