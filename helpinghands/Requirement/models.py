from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class NGO_admin(models.Model):
    email_id=models.EmailField(null=True)
    NGO_password=models.CharField(max_length=50,null=True)
    NGO_id=models.CharField(max_length=50,null=True)
    NGO_name=models.CharField(max_length=50,null=True)
    NGO_address=models.CharField(max_length=1000,null=True)
  
    def __str__(self):
        return self.NGO_name

class Requirement(models.Model):
    email=models.ForeignKey(NGO_admin,on_delete=models.CASCADE,null=True)
    requirement_type=models.CharField(max_length=20)
    requirement_quantity=models.CharField(max_length=10)
    requirement_name=models.CharField(max_length=20)
    requirement_description=models.CharField(max_length=1000)
    requirement_postedAt=models.DateTimeField(default = timezone.now)

    def __str__(self):
        return self.requirement_type

class Donation(models.Model):
    doner_email=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    donation_type=models.CharField(max_length=20)
    donation_name=models.CharField(max_length=20)
    donation_quantity=models.CharField(max_length=20)
    donation_date=models.DateTimeField(default = timezone.now)

    def __str__(self):
        return self.donation_name