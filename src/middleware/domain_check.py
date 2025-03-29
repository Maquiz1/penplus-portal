# filepath: /home/maquiz/projects/Hospital_Systems/penplus-edc/src/middleware/domain_check.py
from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings


class DomainCheckMiddleware:
    """
    Middleware for handling different app domains.
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        host = request.get_host().split(':')[0]  # Extract the domain without port

        # Map domains to their respective URL configurations
        domain_to_urlconf = {
            "penplus.com": "penplus.urls",
            "pedx.com": "pedx.urls",
            "logbook.com": "logbook.urls",
        }

        if host in domain_to_urlconf:
            # Set the URL configuration for the recognized domain
            request.urlconf = domain_to_urlconf[host]
        else:
            # Render the base.html template with the context for unrecognized domains
            context = {
                'penplus_domain': settings.PENPLUS_DOMAIN,
                'pedx_domain': settings.PEDX_DOMAIN,
                'logbook_domain': settings.LOGBOOK_DOMAIN,
            }
            return render(request, 'base.html', context)

        # Proceed with the request if the domain is recognized
        return self.get_response(request)
