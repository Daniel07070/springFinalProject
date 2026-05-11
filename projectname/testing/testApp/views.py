from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .models import Chord, UserUpload



def home(request):
	featured_chords = Chord.objects.filter(
	name__in=["C Major", "G Major", "A Minor"]
	)

	chords = None

	if request.GET.get("q"):
		query = request.GET.get("q")
		chords = Chord.objects.filter(name__icontains=query)

	return render(request, "home.html", {
		"chords": chords,
		"featured_chords": featured_chords,
	})

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

@login_required
def upload(request):
	if request.method == "POST":
		file = request.FILES.get('media')

		if file:
			UserUpload.objects.create(
				user=request.user,
				file=file
			)
	return redirect('profile')

@login_required
def profile(request):
	uploads = UserUpload.objects.filter(user=request.user).order_by('-uploaded_at')

	return render(request, 'profile.html', {
		'user_obj': request.user,
		'uploads': uploads

	})

def bookmarks(request):
	return render(request, 'bookmarks.html')	
	