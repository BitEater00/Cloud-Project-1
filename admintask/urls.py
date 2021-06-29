from django.urls import path
from admintask import views

urlpatterns = [
    path('' , views.adminLanding),
    path('create', views.createClub)
]