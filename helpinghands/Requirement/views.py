from django.shortcuts import render
from .models import Requirement,Donation
from datetime import datetime

# Create your views here.
def require_form(request):
    return render(request,'Requirement/requirement.html')

def about(request):
    return render(request,'Requirement/about.html')


def receipt(request):
    if request.method=='POST':
        product_type=request.POST.get('type')
        product_quantity=request.POST.get('Quantity')
        product_name=request.POST.get('ProductName')
        product_description=request.POST.get('desc')
        print(product_type,product_quantity,product_name,product_description)
        requirement = Requirement(
        requirement_type=product_type,
        requirement_quantity= product_quantity,
        requirement_name=product_name,
        requirement_description=product_description,
        )
        requirement.save()
        context={
            'type':product_type,
            'quantity':product_quantity,
            'Name':product_name,
            'desc': product_description,
            'datetime':datetime.now(),
        }
    return render(request,'Requirement/receipt.html',context)

def donation_form(request):
    return render(request,'Requirement/donation.html')

def donation_form_receipt(request):
    if request.method=='POST':
        donation_type=request.POST.get('type')
        donation_quantity=request.POST.get('Quantity')
        donation_name=request.POST.get('ProductName')
        donation = Donation(
            donation_type=donation_type,
            donation_name=donation_name,
            donation_quantity=donation_quantity,
        )
        donation.save()
        context={
            'type':donation_type,
            'quantity':donation_quantity,
            'datetime':datetime.now(),
        }
    return render(request,'Requirement/donation-receipt.html',context)