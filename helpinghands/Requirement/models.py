from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class NGO(models.Model):
    email_id=models.EmailField(null=True)
    NGO_password=models.CharField(max_length=50)
    NGO_id=models.CharField(max_length=50)
    NGO_name=models.CharField(max_length=50)
    NGO_address=models.CharField(max_length=1000)
  
def __str__(self):
        return self.NGO_name


class Requirement(models.Model):
    email=models.ForeignKey(NGO,on_delete=models.CASCADE,null=True)
    requirement_type=models.CharField(max_length=20)
    requirement_quantity=models.CharField(max_length=10)
    requirement_name=models.CharField(max_length=20)
    requirement_description=models.CharField(max_length=1000)
    requirement_postedAt=models.DateTimeField(default = timezone.now)

    def __str__(self):
        return self.requirement_type
