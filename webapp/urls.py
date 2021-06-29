"""webapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path , include
from webapp import views

urlpatterns = [
    path('' , views.index),
    path('techteam/', admin.site.urls),
    path('user/' , include('userauth.urls')),
    path('student/' , include('student.urls')),
    path('club/' , include('club.urls')),
    path('event/' , include('event.urls')),
    path('admin/' , include('admintask.urls')),
]

handler404 = 'webapp.views.error_404'
handler500 = 'webapp.views.error'
handler403 = 'webapp.views.error_403'
handler400 = 'webapp.views.error_403'