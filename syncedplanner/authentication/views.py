from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils.safestring import mark_safe


from .forms import LoginForm, RegisterForm

# Create your views here.


def sign_in(request):
    if not request.user.is_authenticated:
        if request.method == 'GET':
            form = LoginForm()
            return render(request, 'authentication/login.html', {'form': form})
        elif request.method == 'POST':
            form = LoginForm(data=request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                user = authenticate(request, username=username, password=password)
                if user:
                    login(request, user)
                    messages.success(request, f'Hi {username.title()}, welcome back!')
                    return redirect('index')

            messages.error(request, f'Invalid username or password')
            return render(request, 'authentication/login.html', {'form': form})
    else:
        logout_url = reverse('logout')
        messages.warning(request, mark_safe(
            f'You are already logged, {request.user.get_username().title()}. <a href="{logout_url}">Logout</a>')
        )
        return redirect('index')


def sign_up(request):
    if not request.user.is_authenticated:
        if request.method == 'GET':
            form = RegisterForm()
            return render(request, 'authentication/register.html', {'form': form})

        elif request.method == 'POST':
            form = RegisterForm(data=request.POST)

            if form.is_valid():
                new_user = form.save()
                messages.success(request, f'Welcome {new_user.get_username().title()}, nice to meet you !')
                return redirect('login')

            messages.error(request, f'An error occurred while creating your account')
            return render(request, 'authentication/register.html', {'form': form})
    else:
        logout_url = reverse('logout')
        messages.warning(request, mark_safe(
            f'You are already logged, {request.user.get_username().title()}. <a href="{logout_url}">Logout</a>')
        )
        return redirect('index')


def sign_out(request):
    logout(request)
    messages.success(request, f'You have been logged out.')
    return redirect('login')
