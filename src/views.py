from django.shortcuts import render
from django.conf import settings

def landing(request):
    """
    Renders the landing page with links to the app domains.
    """
    context = {
        'penplus_domain': settings.PENPLUS_DOMAIN,
        'pedx_domain': settings.PEDX_DOMAIN,
        'logbook_domain': settings.LOGBOOK_DOMAIN,
    }
    return render(request, 'landing.html', context)