from django.shortcuts import render
from .models import Hostel

# Ei function-ta missing chilo tai error ashche
def front_page(request):
    return render(request, 'front_page.html')

def hostel_list(request):
    hostels = Hostel.objects.all()
    return render(request, 'hostel_list.html', {'hostels': hostels})