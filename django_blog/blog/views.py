from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from .models import Post
from .forms import CustomUserCreationForm, ProfileForm, PostForm


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
			return redirect("blog:profile")
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
			return redirect("blog:profile")
	else:
		form = ProfileForm(instance=user)
	return render(request, "blog/profile.html", {"form": form})


class PostListView(ListView):
	model = Post
	template_name = "blog/posts_list.html"
	context_object_name = "posts"
	ordering = ["-published_date"]


class PostDetailView(DetailView):
	model = Post
	template_name = "blog/post_detail.html"


class PostCreateView(LoginRequiredMixin, CreateView):
	model = Post
	form_class = PostForm
	template_name = "blog/post_form.html"

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Post
	form_class = PostForm
	template_name = "blog/post_form.html"

	def test_func(self):
		post = self.get_object()
		return self.request.user == post.author


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = Post
	template_name = "blog/post_confirm_delete.html"
	success_url = reverse_lazy("blog:posts")

	def test_func(self):
		post = self.get_object()
		return self.request.user == post.author
