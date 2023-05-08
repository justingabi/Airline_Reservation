from rest_framework import serializers
from reservations.models import Flight, Reservation

class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = ['flight_number', 'departure_location', 'arrival_location', 'departure_time', 'arrival_time', 'available_seats']

class ReservationSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    flight = serializers.StringRelatedField()

    class Meta:
        model = Reservation
        fields = ['user', 'flight', 'booking_date', 'trip_type']