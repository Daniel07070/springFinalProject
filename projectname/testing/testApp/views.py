from django.shortcuts import render, redirect
from .models import Chord


def home(request):
	query = request.GET.get('q')

	if query: # if user typed something in search then
		chords = Chord.objects.filter(name__icontains=query)
	else:
		chords = Chord.objects.none()

	return render(request, 'home.html',{'chords': chords}) #makes chords available for template


