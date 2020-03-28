from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from user.models import Blog
from django.http import HttpResponse
from django.views.generic import CreateView, UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

class Add_Blog(LoginRequiredMixin, CreateView):
	model = Blog
	template_name = 'blog/add.html'
	context_object_name = 'blog'
	fields = ['heading', 'body']

	def form_valid(self,form):
		form.instance.author = self.request.user
		return super().form_valid(form)

class Update_Blog(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Blog
	template_name = 'blog/add.html'
	context_object_name = 'blog'
	fields = ['heading', 'body']

	def form_valid(self,form):
		form.instance.author = self.request.user
		return super().form_valid(form)

	def test_func(self):
		if self.request.user == self.get_object().author:
			return True
		return False

class Delete_Blog(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = Blog
	context_object_name = 'blog' 
	success_url = '/dash'
	template_name = 'blog/blog_confirm_delete.html'
	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True
		return False
