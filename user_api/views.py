from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'user_api/index.html')

def login(request):
    return render(request, 'user_api/login.html')

def profile(request):
    return render(request, 'user_api/profile.html')

