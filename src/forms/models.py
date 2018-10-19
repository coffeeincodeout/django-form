from django.db import models

# Create your models here.
integer_list = ((n, n) for n in range(10))


class rsvp(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(blank=False)
    guests = models.IntegerField(choices=integer_list)
    time_stamp = models.DateTimeField(auto_now=True)
    house_guest = models.BooleanField(default=False)
