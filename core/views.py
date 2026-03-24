from django.shortcuts import render
from .models import Hostel

def front_page(request):
    return render(request, 'front_page.html') # Page 1

def hostel_list(request):
    hostels = Hostel.objects.all()
    return render(request, 'hostel_list.html', {'hostels': hostels}) # Page 5

def registration(request):
    return render(request, 'registration.html')

def login_view(request):
    return render(request, 'login.html')