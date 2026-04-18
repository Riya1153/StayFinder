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