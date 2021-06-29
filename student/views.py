from django.shortcuts import render , HttpResponse
from django.contrib.auth.decorators import login_required
from grpcheckerview import group_required
from event import datahandler as evedata
import pytz
from datetime import datetime
# Create your views here.

tz = pytz.timezone('Asia/Kolkata')
today = datetime.now(tz)

@login_required(login_url="/user/login")
@group_required("Studentgrp")
def student(request):
    registeredEvents = evedata.getRegisteredEventforStudent(request.user.username)
    clubEvent = evedata.getSubscribedEventforStudent(request.user.username , today)
    context = {"registeredEvents" : registeredEvents , "clubEvent" : clubEvent}
    return render(request , 'studentlanding.html' , context)