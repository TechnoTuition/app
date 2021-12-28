from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from .forms import UserRegistrationForm,LoginForm,ForgotPasswordForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from django.core.mail import send_mail

#from django.core.exceptions import ObjectsDoseNotExist

# Create your views here.
def index(request):
  print(request.user.is_active)
  return render(request,'home/index.html')

#Login Form control
def user_login(request):
  if request.user.is_authenticated:
      messages.info(request,'You have Already Loging')
      return redirect("/user")
  elif request.method == "POST":
    form = LoginForm(request.POST)
    if form.is_valid():
      username = request.POST["username"]
      password = request.POST["password"]
      user = authenticate(request,username=username,password=password)
      if user is not None:
        login(request,user)
        return redirect("/user/")
      else:
        messages.error(request,'Invalid credentials! Please try again ')
        return redirect("/login")
        
  else:
    form = LoginForm()
    
  #form = LoginForm()
  return render(request,'home/login.html',{'form':form})
  
# user signup page 
def user_signup(request):
  if request.user.is_authenticated:
      messages.info(request,'You have Already Loging')
      return redirect("/user")
  elif request.method == "POST":
    form = UserRegistrationForm(request.POST)
    if form.is_valid():
      username = request.POST["username"]
      email = request.POST["email"]
      password = request.POST["password"]
      print(username,email,password)
      useremail = User.objects.filter(email=email)
      userName = User.objects.filter(username=username)
      if useremail:
        messages.info(request,'You have already email account registerd !')
        return redirect("/signup")
      elif userName :
        messages.info(request,'Username must be unique')
        return redirect('/signup')
      else:
        user = User.objects.create_user(username, email, password)
        user.save()
        messages.success(request,'Your account Hase been created successfully')
        subjects = "Welcome to OkEarn"
        message = f"Hi {user.username} thank you for creating your account In OkEarn"
        email_from = settings.EMAIL_HOST_USER
        recipent = [user.email,]
        send_mail(subjects,message,email_from,recipent,)
        return redirect("/signup")
  
  else:
    form = UserRegistrationForm()
  return render(request,'home/signup.html',{'form':form})


# Logout User
def user_logout(request):
  logout(request)
  return redirect("/login/")

#Forgot password
def user_forgotpassword(request):
  if request.method == "POST":
    form = ForgotPasswordForm(request.POST)
    if form.is_valid():
      username = request.POST["username"]
      newpassword = request.POST["newpassword"]
      print(username,newpassword)
      
      try:
        user = User.objects.get(username=username)
        user.set_password(newpassword)
        user.save()
        messages.success(request,'Password hase change successfully !')
        return redirect("/login/")
      except ObjectDoesNotExist:
        #print('data not exist ')
        messages.warning(request,'Username Not Found !')
        
        return redirect("/forgotpassword/")
  else:
    form = ForgotPasswordForm()
  return render(request,'home/forgotpassword.html',{'form':form})
