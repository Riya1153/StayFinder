from django.contrib import admin
from django.urls import path
from core.views import hostel_list, front_page, registration, login_view
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', front_page, name='front_page'),
    path('hostels/', hostel_list, name='hostel_list'),
    path('registration/', registration, name='registration'),
    path('login/', login_view, name='login'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)