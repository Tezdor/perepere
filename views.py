from django.shortcuts import render
from .forms import *
from .models import User, Nyanya, Booking
from django.views.generic import CreateView, ListView

class RegisterView(CreateView):
    success_url = '/login/'
    form_class = RegisterForm
    template_name = 'register.html'

class BookingView(CreateView):
    success_url = '/'
    form_class = BookingForm
    template_name = 'booking.html'
    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.booking_status = '1'
        return super().form_valid(form)
    
class DashboardView(ListView):
    model = Nyanya
    template_name = 'dashboard.html'

class Zayavki(ListView):
    model = Booking
    template_name = 'zayavki.html'
    def get_queryset(self):
        return Booking.objects.filter(user = self.request.user)
    