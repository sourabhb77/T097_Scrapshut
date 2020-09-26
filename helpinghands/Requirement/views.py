from django.shortcuts import render
from .models import Requirement

# Create your views here.
def require_form(request):
    return render(request,'Requirement/requirement.html')

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
    return render(request,'Requirement/receipt.html')
