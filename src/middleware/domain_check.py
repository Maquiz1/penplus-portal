# filepath: /home/maquiz/projects/Hospital_Systems/penplus-edc/src/middleware/domain_check.py
from django.shortcuts import render


class DomainCheckMiddleware:
    """
    MIDDLE WARE FOR DIFFERENT APP DOMAINS
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
            request.urlconf = domain_to_urlconf[host]
        else:
            # return HttpResponse("Unknown domain", status=404)
            return render(request, 'base.html')

        return self.get_response(request)
