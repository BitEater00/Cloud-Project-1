from django.urls import path
from userauth import views

urlpatterns = [
    path('login/', views.loginuser),
    path('signup/' , views.signup),
    path('signout/' , views.logoutuser),
    path('changepassword/' , views.changepassword),
    path('profile/' , views.loadprofile),
]