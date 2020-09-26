from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import CustomUserForm
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout

def register(request):
    form = CustomUserForm()

    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            
            form.save()
            user = form.cleaned_data.get('first_name')
            messages.success(request, 'Welcome '+ user+',')
            return redirect('accounts-login')

    return render(request, 'accounts/register.html', {'form':form})

def register_ngo(request):
    form = CustomUserForm()
    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('first_name')
            messages.success(request, 'Welcome '+ user+',')
            return redirect('accounts-login')
    return render(request, 'accounts/register_ngo.html', {'form':form})

def about(request):
    return render(request, 'accounts/about.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user1 = authenticate(request, username=username, password=password)

        if user1 is not None:
            auth_login(request, user1)
            return redirect('accounts-home')
        else:
            messages.info(request, 'Username or password is incorrect')



    return render(request, 'accounts/login.html')

def logout(request):
    auth_logout(request)
    return redirect('accounts-login')

def home(request):
    return render(request, 'accounts/home.html')

def description(request):
    return render(request, 'accounts/description.html')