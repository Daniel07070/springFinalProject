from django.shortcuts import render, redirect
from .models import Chord


def home(request):
	query = request.GET.get('q')
	chords = Chord.objects.all() #gets all the chords in the database

	if query: # if user typed something in search then
		chords = chords.filter(name_icontains=query)

	return render(request, 'home.html',{'chords': chords}) #makes chords available for template


