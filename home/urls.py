from django.urls import path
from home import views 
urlpatterns = [
    path('', views.index,name="index"),
    path('login/',views.user_login,name="user_login"),
    path('signup/',views.user_signup,name="user_signup"),
    path('logout/',views.user_logout,name="user_logout"),
    path('forgotpassword/',views.user_forgotpassword,name="user_forgotpassword"),
]
