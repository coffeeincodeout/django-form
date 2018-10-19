from django.shortcuts import render
from django.http import JsonResponse
from .forms import RsvpForm

# Create your views here.


def home(request):
    form = RsvpForm()
    return render(request, 'index.html', {'form': form})


def rsvpform(request):
    if request.method == 'POST':
        form = RsvpForm(request.POST)
        if form.is_valid():
            form.save()
            form = RsvpForm()
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'error': form.errors})

    else:
        form = RsvpForm()
    return render(request, 'index.html', {'form': form})
