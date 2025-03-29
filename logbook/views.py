from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # Example response for Logbook
    return render(request, 'logbook/dashboard.html')

def records(request):
    # Example of rendering a template for Logbook
    return render(request, 'logbook/records.html')
