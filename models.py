from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    full_name = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS =  ['full_name', 'phone', 'username']

class Booking(models.Model):
    pm = {
        '1': 'наличные',
        '2': 'карта',
    }
    bs = {
        '1': 'в разработке',
        '2': 'отменено',
        '3': 'подтверждено',
    }
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    nyanya = models.ForeignKey('Nyanya', on_delete=models.CASCADE)
    payment_method = models.CharField(max_length=20, choices=pm)
    booking_status = models.CharField(max_length=20, choices=bs)
    data = models.DateTimeField()
    cancel = models.TextField(blank=True)

class Nyanya(models.Model):
    detii = {
        '1': 'малыши',
        '2': 'школьники',
        '3': 'подростки',
    }
    name = models.CharField(max_length=20, blank=True)
    phone = models.CharField(max_length=20)
    age = models.IntegerField()
    deti = models.CharField(max_length=20, choices=detii)

    def __str__(self):
        return self.name
    

