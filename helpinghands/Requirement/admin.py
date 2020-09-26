from django.contrib import admin
from Requirement.models import NGO_admin,Requirement,Donation

# Register your models here.
admin.site.register(NGO_admin)
admin.site.register(Requirement)
admin.site.register(Donation)