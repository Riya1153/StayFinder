from django.contrib import admin
from django.urls import path
from core.views import hostel_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hostels/', hostel_list, name='hostel_list'),
]