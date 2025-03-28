from django.http import HttpResponse
from django.urls import path

# Default view if no matching domain
def default_view(request):
    return HttpResponse("Unknown domain")

urlpatterns = [
    path("", default_view),  # Fallback view
]


# urlpatterns = [
#     path('penplus/', include('penplus.urls')),  # Penplus URLs
#     path('pedx/', include('pedx.urls')),       # Pedx URLs
#     path('logbook/', include('logbook.urls')), # Logbook URLs
# ]