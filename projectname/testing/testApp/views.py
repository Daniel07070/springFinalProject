from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .models import Chord


def home(request):
	query = request.GET.get('q')

	if query: # if user typed something in search then
		chords = Chord.objects.filter(name__istartswith=query)
	else:
		chords = Chord.objects.none()

	return render(request, 'home.html',{'chords': chords}) #makes chords available for template

def register(request):
	if request.method == "POST":
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request, "Account created successfully")
			return redirect ("login")
	else:
		form = UserCreationForm()

	return render(request, "register.html", {"form":form})
