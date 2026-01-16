from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class JobApplication(models.Model):
    full_name = models.CharField(max_length=300)
    email = models.EmailField()
    resume = models.FileField(upload_to='resume/')
    profile_picture = models.ImageField(upload_to ='profile_pics/',blank=True,null=True)
    cover_letter = models.TextField()
    applied_on = models.DateTimeField(auto_now_add=True)