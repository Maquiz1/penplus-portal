from django.http import HttpResponse
from django.urls import path
from django.shortcuts import render
from django.conf import settings

def default_view(request):
    context = {
        'penplus_domain': settings.PENPLUS_DOMAIN,
        'pedx_domain': settings.PEDX_DOMAIN,
        'logbook_domain': settings.LOGBOOK_DOMAIN,
    }
    return render(request, 'base.html', context)

urlpatterns = [
    path("", default_view),  # Fallback view
]