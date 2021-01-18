from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout


def home(request):
    return render(request, 'index.html')


def signupuser(request):
    if request.method == 'GET':
        return render(request, 'signupuser.html', {'form': UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:

                user = User.objects.create_user(
                    request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('dashboard')
            except IntegrityError:
                return render(request, 'signupuser.html', {'form': UserCreationForm(), 'error': 'Username is unavailable'})
        else:
            return render(request, 'signupuser.html', {'form': UserCreationForm(), 'error': 'Passwords didn\'t match'})


def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')


def dashboard(request):
    return render(request, 'dashboard.html')
