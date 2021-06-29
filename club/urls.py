from django.urls import path
from club import views

urlpatterns = [
    path('' , views.club),
    path('id/<str:id>' , views.clubforid),
    path('create' , views.createEvent),
    path('clubs' , views.allclubsloaded),
]