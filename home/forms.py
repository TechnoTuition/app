from django import forms
class UserRegistrationForm(forms.Form):
  username = forms.CharField(label = 'Username',max_length=15 ,min_length=4,required=True,widget=forms.TextInput(attrs={'class': 'form-control'}))
  email = forms.EmailField(label='Email',widget=forms.TextInput(attrs={'class': 'form-control'}))
  password = forms.CharField(label='Password',max_length=50,min_length=8,widget=forms.TextInput(attrs={'class': 'form-control'}))

class LoginForm(forms.Form):
  username = forms.CharField(label = 'Username',max_length=15 ,min_length=4,required=True,widget=forms.TextInput(attrs={'class': 'form-control'}))
  password = forms.CharField(label='Password',max_length=50,min_length=8,widget=forms.TextInput(attrs={'class': 'form-control'}))
  
class ForgotPasswordForm(forms.Form):
  username = forms.CharField(label = 'Username',max_length=15 ,min_length=4,required=True,widget=forms.TextInput(attrs={'class': 'form-control'}))
  
  newpassword = forms.CharField(label='New Password',max_length=50,min_length=8,widget=forms.TextInput(attrs={'class': 'form-control'}))
  