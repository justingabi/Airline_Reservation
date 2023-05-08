from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Flight, Reservation
from airline_reservation.forms import FlightForm, ReservationForm

def is_admin(user):
    return user.is_superuser

@login_required
def book_flight(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST, user=request.user)
        if form.is_valid():
            form.save()
            return redirect('view_flights')
    else:
        form = ReservationForm(user=request.user)
    return render(request, 'reservations/book_flight.html', {'form': form})

@login_required
def view_flights(request):
    reservations = Reservation.objects.filter(user=request.user)
    return render(request, 'reservations/view_flights.html', {'reservations': reservations})

@user_passes_test(is_admin)
def add_flight(request):
    if request.method == 'POST':
        form = FlightForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_all_flights')
    else:
        form = FlightForm()
    return render(request, 'reservations/add_flight.html', {'form': form})

@user_passes_test(is_admin)
def view_all_flights(request):
    flights = Flight.objects.all()
    return render(request, 'reservations/view_all_flights.html', {'flights': flights})

# Create your views here.
