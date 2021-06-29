from django.shortcuts import render , HttpResponse
from event import datahandler as dataconn
from student import datahandler as studata
from django.contrib.auth.decorators import login_required
from grpcheckerview import group_required , group_not_required
from django.http import *
import traceback
import pytz
from datetime import datetime
from messagequeue import uploadQueueEvent

tz = pytz.timezone('Asia/Kolkata')
today = datetime.now(tz)

# Create your views here.
@group_not_required("Clubgrp" , "Techgrp")
def events(request):
    try:
        if request.method == 'POST':
            if request.POST['action'] == "Register":
                studentId = request.POST['studentId']
                eventId = request.POST['eventId']
                dataconn.addStudentRegistration(studentId=studentId , eventId=eventId)
                stu = studata.getStudent(request.user.username)
                uploadQueueEvent(stu['studentEmail'])

        allevents = dataconn.getAllLiveEvent(today)
        subeve = dataconn.getSubscribedEventforStudent(request.user.username , today)
        context = {"events" : allevents , "clubEvent" :subeve} 
        return render(request , 'events.html' , context)
    except:
        traceback.print_exc()
        return HttpResponseServerError()


@group_not_required("Clubgrp" , "Techgrp")
def event(request , id = 0):

    if(id == 0):
        raise Http404()
    
    if request.method == 'POST':
        if request.POST['action'] == "Register":
            studentId = request.POST['studentId']
            eventId = request.POST['eventId']
            dataconn.addStudentRegistration(studentId=studentId , eventId=eventId)
            stu = studata.getStudent(request.user.username)
            uploadQueueEvent(stu['studentEmail'])
            
        elif request.POST['action'] == "Unregister":
            studentId = request.POST['studentId']
            eventId = request.POST['eventId']
            dataconn.removeStudentRegistration(studentId=studentId , eventId= eventId)

    try:
        event = dataconn.getEvent(id)
        if event is None:
            traceback.print_exc()
            raise Exception
        
        context = {"event" : event}
        return render(request , 'event.html' , context)
    except:
        traceback.print_exc()
        raise Http404()

@login_required(login_url = '/user/login/')
@group_required("Clubgrp")
def participant(request , id = 0):
    if id == 0:
        raise Http404()
    
    studentData = dataconn.getParticipant(id)
    if studentData is None:
        return render(request , 'participate.html')
    return render(request , 'participate.html' , context={"student":studentData})