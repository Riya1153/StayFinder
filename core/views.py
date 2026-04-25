from django.shortcuts import render,redirect
from .models import Hostel
from .forms import BookingSearchForm

def front_page(request):
    return render(request, 'front_page.html')  # Page 1

def registration(request):
    return render(request, 'registration.html')

def login_view(request):
    return render(request, 'login.html')

def add_hostel(request):
    return render(request, 'add_hostel.html')

def dashboard(request):

    if request.method == 'POST':
    # This is where you would normally save the Name, Email, etc.
    # After saving, we send them to the search page
      return redirect('search_page')

    # If they are just looking at the page, show them the dashboard


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
    form = BookingSearchForm(request.GET or None)



    return render(request, 'searching_sector.html', {'form': form})

def verify_code(request):
    return render(request, 'verify_code.html')

def search_view(request):
    return render(request, 'search.html')




def requirement(request):
    if request.method == 'POST':
        # Logic to handle the form data will go here later
        # name = request.POST.get('name')
        # email = request.POST.get('email')
        # message = request.POST.get('requirement')
        return redirect('search_page')  # Redirect back after submission

    return render(request, 'requirement.html')

def payment_process(request):
    if request.method == 'POST':

        return redirect('payment_method')
    return render(request, 'payment_process.html')

def payment_method(request):
    if request.method == 'POST':
        # Logic for handling complaints or payment choices can go here
        return redirect('search_page')
    return render(request, 'payment_method.html')








