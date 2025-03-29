# filepath: /home/maquiz/projects/Hospital_Systems/penplus-edc/src/middleware/domain_check.py
from django.shortcuts import render
from django.conf import settings


class DomainCheckMiddleware:
    """
    Middleware for handling different app domains and rendering appropriate templates.
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        host = request.get_host().split(':')[0]  # Extract the domain without port

        # Map domains to their respective URL configurations and base templates
        domain_to_config = {
            "penplus.com": {
                "urlconf": "penplus.urls",
                "base_template": "penplus/base.html",
            },
            "pedx.com": {
                "urlconf": "pedx.urls",
                "base_template": "pedx/base.html",
            },
            "logbook.com": {
                "urlconf": "logbook.urls",
                "base_template": "logbook/base.html",
            },
        }

        if host in domain_to_config:
            # Set the URL configuration for the recognized domain
            request.urlconf = domain_to_config[host]["urlconf"]
        else:
            # Render the appropriate base template for unrecognized domains
            context = {
                'penplus_domain': settings.PENPLUS_DOMAIN,
                'pedx_domain': settings.PEDX_DOMAIN,
                'logbook_domain': settings.LOGBOOK_DOMAIN,
            }
            # Use a default base template for unrecognized domains
            return render(request, "base.html", context)
            # return render(request, "base.html")


        # Proceed with the request if the domain is recognized
        return self.get_response(request)
