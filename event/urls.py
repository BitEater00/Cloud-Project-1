from django.urls import path 
from event import views

urlpatterns = [
    path('' , views.events),
    path('registration/<str:id>' , views.participant),
    path('<str:id>' , views.event),
]