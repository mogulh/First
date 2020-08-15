from django.shortcuts import render


# Create your views here.

def login(request):
    context = {}
    return render(request, 'users/login.html', context)


def signup(request):
    context = {}
    return render(request, 'users/signup.html', context)


def home(request):
    context = {}
    return render(request, 'users/home.html', context)


def dashboard(request):
    context = {}
    return render(request, 'users/dashboard.html', context)



def profile(request):
    context = {}
    return render(request, 'users/profile.html', context)


def settings(request):
    context = {}
    return render(request, 'users/settings.html', context)



