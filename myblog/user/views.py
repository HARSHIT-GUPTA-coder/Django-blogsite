from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from .models import Blog
from django.http import HttpResponse
from django.views.generic import CreateView

def home(request):
	if request.method=='POST':
		if 'signup' in request.POST:
			form = UserCreationForm(request.POST)
			if form.is_valid():
				form.save()
				username = form.cleaned_data.get('username')
				messages.success(request, f'Your account has been created! You will now be able to log in', extra_tags='signup')
				return redirect('dash')
			else:
				messages.warning(request, "Invalid username given for registration or the passwords entered don't match.", extra_tags='signup')
		elif 'logout' in request.POST:
			logout(request)
			messages.success(request, f'You have successfully logged out')
			return redirect('home')
		else:
			form = AuthenticationForm(request=request, data=request.POST)
			if form.is_valid():
				username = form.cleaned_data.get('username')
				password = form.cleaned_data.get('password')
				user = authenticate(username=username, password=password)
				if user is not None:
					login(request, user)
					messages.info(request, f"You are now logged in as {username}",  extra_tags='login')
					return redirect('dash')
				else:
					messages.warning(request, "Invalid username or password.", extra_tags='login')
			else:
				messages.warning(request, "Invalid username or password.", extra_tags='login')
		
	form2=UserCreationForm()
	form1=AuthenticationForm()
	cont = {
	'title' : 'Home',
	'blogs' :  Blog.objects.all().order_by('-id'),
	'form1' : form1,
	'form2' : form2
	}	
	return render(request,'user/home.html',cont)

@login_required
def dash(request):
	if request.method=='POST':
		logout(request)
		messages.success(request, f'You have successfully logged out')
		return redirect('home')
	context = {
	'title' : 'Dashboard',
	'blogs' :  request.user.blog_set.all().order_by('-id'),
	}	
	return render(request,'user/dash.html',context)


