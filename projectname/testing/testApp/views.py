from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Chord, UserUpload



def home(request):
	featured_chords = Chord.objects.filter(
	name__in=["C Major", "G Major", "A Minor"]
	)
	query = request.GET.get('q')
	#chords = None

	if query:
		chords = Chord.objects.filter(name__icontains=query)
		users = User.objects.filter(username__icontains=query)
	else:
		chords = Chord.objects.none()
		users = User.objects.none()

	return render(request, "home.html", {
		"chords": chords,
		"users": users,
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
			print(form.errors)
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
	return redirect('profile', username=request.user.username)

@login_required
def profile(request, username):
	user_obj = User.objects.get(username=username)
	uploads = UserUpload.objects.filter(user=user_obj).order_by('-uploaded_at')
	return render(request, 'profile.html', {
		'user_obj': user_obj,
		'uploads': uploads

	})

def bookmarks(request):
	return render(request, 'bookmarks.html')	
	