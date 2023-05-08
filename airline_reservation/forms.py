from django import forms
from reservations.models import Flight, Reservation

class FlightForm(forms.ModelForm):
    class Meta:
        model = Flight
        fields = ('flight_number', 'departure_location', 'arrival_location', 'departure_time','arrival_time', 'available_seats')

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['flight', 'trip_type']

    def init(self, args, user=None, **kwargs):
        super().init(args, **kwargs)
        self.fields['flight'].queryset = Flight.objects.exclude(available_seats=0)
        if user is not None:
            self.instance.user = user