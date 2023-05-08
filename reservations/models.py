from django.db import models
from django.contrib.auth.models import User


class Flight(models.Model):
    flight_number = models.CharField(max_length=10, unique=True)
    departure_location = models.CharField(max_length=100)
    arrival_location = models.CharField(max_length=100)
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()
    available_seats = models.IntegerField()

    def str(self):
        return self.flight_number

class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    booking_date = models.DateTimeField(auto_now_add=True)
    trip_type = models.CharField(max_length=20, choices=(("round_trip", "Round Trip"), ("one_way", "One Way")))

    def str(self):
        return f"{self.user.username} - {self.flight.flight_number}"
