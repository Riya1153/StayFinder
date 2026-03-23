from django.contrib import admin
from django.urls import path
from core.views import hostel_list, front_page # front_page import koro

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', front_page, name='front_page'), # Eita empty path thakte hobe
    path('hostels/', hostel_list, name='hostel_list'),
]