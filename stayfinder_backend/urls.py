from django.contrib import admin
from django.urls import path
from core.views import hostel_list
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hostels/', hostel_list, name='hostel_list'),
]

# Media files setup
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)