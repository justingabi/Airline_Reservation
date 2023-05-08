from django.urls import path
from . import views

urlpatterns = [
    path('book_flight/', views.book_flight, name='book_flight'),
    path('view_flights/', views.view_flights, name='view_flights'),
    path('add_flight/', views.add_flight, name='add_flight'),
    path('view_all_flights/', views.view_all_flights, name='view_all_flights'),
]