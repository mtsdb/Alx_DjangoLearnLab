from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from .models import Post
from .forms import CustomUserCreationForm, ProfileForm


def home(request):
	posts = Post.objects.all().order_by("-published_date")
	return render(request, "blog/home.html", {"posts": posts})


def register(request):
	if request.method == "POST":
		form = CustomUserCreationForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful. You are now logged in.")
			return redirect("profile")
	else:
		form = CustomUserCreationForm()
	return render(request, "blog/register.html", {"form": form})


@login_required
def profile(request):
	user = request.user
	if request.method == "POST":
		form = ProfileForm(request.POST, instance=user)
		if form.is_valid():
			form.save()
			messages.success(request, "Profile updated.")
			return redirect("profile")
	else:
		form = ProfileForm(instance=user)
	return render(request, "blog/profile.html", {"form": form})
