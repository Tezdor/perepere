from django.urls import path, include
from .views import *
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view(template_name = 'login.html')),
    path('logout/', LogoutView.as_view(template_name='logout.html')),
    path('booking/', BookingView.as_view()),
    path('', DashboardView.as_view()),
    path('bookings/', Zayavki.as_view())
]
