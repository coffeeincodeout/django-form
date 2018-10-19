from .models import rsvp
from django import forms
from django.forms import ModelForm


class RsvpForm(forms.ModelForm):
    class Meta:
        model = rsvp
        fields = ['name', 'email', 'guests']
