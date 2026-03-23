from django.contrib import admin
from django.urls import path
from core.views import hostel_list, front_page
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', front_page, name='front_page'),           # http://127.0.0.1:8000/
    path('hostels/', hostel_list, name='hostel_list'), # http://127.0.0.1:8000/hostels/
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)