from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Profile
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.

@login_required
def index(request):
  print(dir(request))
  a = request.user.is_active
  print(a)
  return render(request,"user/index.html")

@login_required
def user_profile(request):
  return render(request,"user/profile.html")
  
  
@login_required
def profile_edit(request,id):
  if request.method == "POST":
    firstname = request.POST.get("firstname")
    lastname = request.POST.get("lastname")
    email = request.POST.get("email")
    profile = request.FILES.get("profile")
    print(request.user)
    print(firstname,lastname,email,profile)
    
    p = Profile(user=request.user,firstname=firstname,lastname=lastname,email=email,profile_pic=profile)
    p.save()
    
    
  else:
    pass
    return render(request,'user/profileEdit.html')
  return render(request,'user/profileEdit.html')