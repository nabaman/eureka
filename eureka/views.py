from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect


def loginView(request):
    print(request.POST)
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request, username=username, password=password)
    if request.method == 'POST':
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request,'invalid username or passsword')
    return render(request, 'unauthenticated/login.html')


def logoutView(request):
    logout(request)
    return redirect('login')