from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
  user = models.OneToOneField(User,on_delete=models.CASCADE)
  firstname = models.CharField(max_length=50,default="Firstname")
  lastname = models.CharField(max_length=80,default="lastname")
  email = models.EmailField(max_length=245,default="default@email.com")
  profile_pic = models.ImageField(upload_to="profile",default="default.png")