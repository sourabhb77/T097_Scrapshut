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
            return redirect('login')

    return render(request, 'accounts/register.html', {'form':form})

def register_ngo(request):
    form = CustomUserForm()
    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('first_name')
            messages.success(request, 'Welcome '+ user+',')
            return redirect('login')
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
            return redirect('home')
        else:
            messages.info(request, 'Username or password is incorrect')



    return render(request, 'accounts/login.html')

def logout(request):
    auth_logout(request)
    return redirect('login')



def description(request):
    return render(request, 'accounts/description.html')

# def donation_form(request):
#     return render(request,'accounts/donation.html')

def donation_form_receipt(request):
    # if request.method=='POST':
    #     donation_type=request.POST.get('type')
    #     donation_quantity=request.POST.get('Quantity')
    #     donation_name=request.POST.get('ProductName')
    #     donation = Donation(
    #         donation_type=donation_type,
    #         donation_name=donation_name,
    #         donation_quantity=donation_quantity,
    #     )
    #     donation.save()
    #     context={
    #         'type':donation_type,
    #         'quantity':donation_quantity,
    #         'datetime':datetime.now(),
    #     }
    return render(request,'accounts/donation-receipt.html')

