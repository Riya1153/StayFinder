from django.contrib import admin
from django.urls import path
from core import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.front_page, name='front_page'),
    path('registration/', views.registration, name='registration'),
    path('login/', views.login_view, name='login'),
    path('forget-password/', views.forget_password, name='forget_password'),
    path('add-hostel/', views.add_hostel, name='add_hostel'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('hostels/', views.hostel_list, name='hostel_list'),
    path('property-details/<int:property_id>/', views.property_details, name='property_details'),
    path('hostels/boys/', views.boys_hostel_view, name='boys_hostel'),
    path('hostels/girls/', views.girls_hostel_view, name='girls_hostel'),
    path('searching-sector/', views.searching_sector, name='searching_sector'),
    path('search/', views.search_view, name='search_page'),
    path('requirement/', views.requirement, name='requirement'),
    path('payment-process/', views.payment_process, name='payment_process'),
    path('payment_method/', views.payment_method, name='payment_method'),
]



# Development static file serving configuration
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)