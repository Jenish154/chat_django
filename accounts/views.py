from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from .forms import RegistrationForm, LoginForm

# Create your views here.
def home(request):
    return render(request, 'accounts/home.html')

def register_user(request):
    user = request.user
    if user.is_authenticated:
        return redirect('home')
    context = {}
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            print("ACCOUNT IS", user)
            login(request, user)
            return redirect('home')
        else:
            context['form'] = form
    context['form'] = form
    return render(request, 'accounts/register.html', context=context)

def login_user(request):
    user = request.user
    if user.is_authenticated:
        return redirect('home')
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(
                username=username,
                password=password
            )
            
            if user is not None:
                print("here")
                login(request, user)
                return redirect('home')
            else:
                print("user is not there buddy")
    return render(request, 'accounts/login.html', {'form': form})

def logout_user(request):
    user = request.user
    if user.is_authenticated:
        logout(request)
        return redirect('home')
    else:
        return redirect('home')