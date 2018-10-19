from django.contrib import admin
from .forms import rsvp

# Register your models here.


@admin.register(rsvp)
class RsvpAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'time_stamp', )
    fields = ['name', 'email',  'guests', 'house_guest']
