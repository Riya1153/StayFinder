from django.shortcuts import render
from .models import Hostel

def front_page(request):
    return render(request, 'front_page.html') # Page 1

def registration(request):
    return render(request, 'registration.html')

def login_view(request):
    return render(request, 'login.html')

def forget_password(request):
    return render(request, 'forget_password.html')

def add_hostel(request):
    return render(request, 'add_hostel.html')

def dashboard(request):
    return render(request, 'dashboard.html')

def hostel_list(request):
    return render(request, 'hostel_list.html')

def property_details(request, property_id):
    return render(request, 'property_details.html', {'id': property_id})

def boys_hostel_view(request):
    return render(request, 'boys_hostel.html')

def girls_hostel_view(request):
    return render(request, 'girls_hostel.html')

def searching_sector(request):
    return render(request, 'searching_sector.html')


def search_results(request):
    category        = request.GET.get('category', '')
    property_type   = request.GET.get('property_type', '')
    tenant_type     = request.GET.get('tenant_type', '')
    residence_type  = request.GET.get('residence_type', '')
    room_type       = request.GET.get('room_type', '')
    gender          = request.GET.get('gender', '')
    price_min       = request.GET.get('price_min', '')
    price_max       = request.GET.get('price_max', '')
    size            = request.GET.get('size', '')
    city            = request.GET.get('city', '')
    location        = request.GET.get('location', '')
    characteristics = request.GET.get('characteristics', '')

    context = {
        'category'        : category,
        'property_type'   : property_type,
        'tenant_type'     : tenant_type,
        'residence_type'  : residence_type,
        'room_type'       : room_type,
        'gender'          : gender,
        'price_min'       : price_min,
        'price_max'       : price_max,
        'size'            : size,
        'city'            : city,
        'location'        : location,
        'characteristics' : characteristics,
    }
    return render(request, 'search_results.html', context)