from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from .forms import TodoForm


def signupuser(request):
    if request.method == 'GET':
        return render(request, 'signup.html', {'form': UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:

                user = User.objects.create_user(
                    request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('dashboard')
            except IntegrityError:
                return render(request, 'signup.html', {'form': UserCreationForm(), 'error': 'Username is unavailable'})
        else:
            return render(request, 'signup.html', {'form': UserCreationForm(), 'error': 'Passwords didn\'t match'})


def loginuser(request):
    if request.method == 'GET':
        return render(request, 'login.html', {'form': AuthenticationForm()})
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'login.html', {'form': AuthenticationForm(), 'error': 'Username and password didn\'t match'})
        else:
            login(request, user)
            return redirect('dashboard')


def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')


def home(request):
    return render(request, 'index.html')


def dashboard(request):
    return render(request, 'dashboard.html')


def create(request):
    if request.method == 'GET':
        return render(request, 'create.html', {'form': TodoForm()})
    else:
        try:
            form = TodoForm(request.POST)
            todo = form.save(commit=False)
            todo.user = request.user
            todo.save()
            return redirect('dashboard')
        except ValueError:
            return render(request, 'create.html', {'form': TodoForm(), 'error': 'Incorrect field entry. Try again.'})
