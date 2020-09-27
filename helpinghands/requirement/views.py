from django.shortcuts import render, redirect , get_object_or_404
from django.http import HttpResponse
from .forms import ProductForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView , DetailView
from .models import requirementModel



# Create your views here.

def home(request):
    views =[1, 2, 3]
    
    return render(request, 'accounts/base_page.html' , {"posts" : views})


def home2(request):
    return render(request, 'accounts/base.html')


@login_required
def fillListForm(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.user = request.user
            form.instance.admin =  request.user
            form.instance.ngo_name = User.objects.get(username=form.instance.admin).first_name
            form.save()
            # username = form.changed_data.get("username")
            # messages.success(request, f'Listing Created')
            return redirect("home")
        else:
            print("add**************************************")
            print(form.errors)
            return redirect("home")

    else:
        form = ProductForm()
    return render(request, 'accounts/st_form.html', {"form" : form , "info" : "form check"})

def logout(request):
    auth_logout(request)
    return redirect('accounts-login')

class listingListView(ListView):
    model = requirementModel
    
    template_name = 'accounts/base_page.html'
    ordering = ['-posted_at']
    context_object_name ="posts"
    paginate_by = 4

class listDetailView(DetailView):
    model = requirementModel
    template_name = 'accounts/list_detail.html'



class ngoListView(ListView):
    model = requirementModel
    template_name = 'accounts/base_page.html'
    context_object_name ="posts"

    # paginate_by =4
    # orderering =['-posted_at']
    
    def get_queryset(self):
        user = self.request.user
        print(user)
        return requirementModel.objects.filter(admin=user).order_by('-posted_at')



# def donation_form_receipt(request):
#     if request.method=='POST':
#         donation_type=request.POST.get('type')
#         donation_quantity=request.POST.get('Quantity')
#         donation_name=request.POST.get('ProductName')
#         donation = Donation(
#             donation_type=donation_type,
#             donation_name=donation_name,
#             donation_quantity=donation_quantity,
#         )
#         # donation.save()
#         print(donation_name)
#         print("*******************")
#         context={
#             'type':donation_type,
#             'quantity':donation_quantity,
#             'datetime':datetime.now(),
#         }
#     return render(request,'accounts/donation-receipt.html')
