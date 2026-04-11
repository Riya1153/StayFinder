from django.contrib import admin
from django.urls import path
from core.views import front_page, registration, login_view, forget_password, add_hostel, dashboard, hostel_list
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', front_page, name='front_page'),
    path('registration/', registration, name='registration'),
    path('login/', login_view, name='login'),
    path('forget-password/', forget_password, name='forget_password'),
    path('add-hostel/', add_hostel, name='add_hostel'),
    path('dashboard/', dashboard, name='dashboard'),
    path('hostels/', hostel_list, name='hostel_list')

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)