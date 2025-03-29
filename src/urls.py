from django.contrib import admin
from django.urls import path, include
from src.views import landing  # Import the landing view from views.py

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin site
    path('', landing, name='landing'),  # Landing page as the default view
    path('penplus/', include('penplus.urls')),  # Penplus app URLs
    path('pedx/', include('pedx.urls')),  # Pedx app URLs
    path('logbook/', include('logbook.urls')),  # Logbook app URLs
]