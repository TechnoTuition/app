from django.urls import path
from user import views 
urlpatterns = [
    path('', views.index,name="index"),
    path('profile/',views.user_profile,name="user_profile"),
    path('profileedit/<int:id>',views.profile_edit,name="profile_edit"),
]
