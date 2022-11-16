from django.urls import path
from . import views


urlpatterns = [
    path('', views.FeedbackList.as_view(), name="home"),
    path('bookings', views.CreateBookingView.as_view(), name="bookings"),
    path('viewbookings', views.ViewBookings.as_view(), name='viewbookings')
]
