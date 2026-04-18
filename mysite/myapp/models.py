from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    phone=models.CharField(max_length=100)
    degree=models.CharField(max_length=50)
    school=models.CharField(max_length=50)
    university=models.CharField(max_length=50)
    summary=models.TextField()
    previous_work=models.TextField()
    skills=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)