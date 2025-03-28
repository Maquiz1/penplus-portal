from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # Example response for Penplus
    return HttpResponse("Welcome to Penplus.com!")

def dashboard(request):
    # Example of rendering a template for Penplus
    return render(request, 'penplus/dashboard.html')
