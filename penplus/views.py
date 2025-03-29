from django.shortcuts import render


def home(request):
    # Example response for Penplus
    return render(request, 'penplus/dashboard.html')


def dashboard(request):
    # Example of rendering a template for Penplus
    return render(request, 'penplus/dashboard.html')
