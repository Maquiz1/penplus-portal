from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # Example response for Pedx
    return render(request, 'pedx/dashboard.html')

def dashboard(request):
    # Example of rendering a template for Pedx
    return render(request, 'pedx/dashboard.html')
