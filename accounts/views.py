from django.shortcuts import render, redirect
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        messages.error( request, 'Testing error message' )
        return redirect('register')
    return render(request, 'accounts/register.html')

def login(request):
    if request.method == 'POST':
        messages.error( request, 'Testing error message' )
        return redirect('login')
    return render(request, 'accounts/login.html')

def logout(request):
    return render(request, 'index')

def dashboard(request):
    return render(request, 'accounts/dashboard.html')