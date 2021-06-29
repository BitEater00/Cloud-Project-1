from django.shortcuts import render , HttpResponse
from django.contrib.auth.decorators import login_required
from grpcheckerview import group_required , group_not_required
from club import datahandler as dataconn
from event import datahandler as eventdataconn
from datetime import datetime
from django.http import *
import pytz
import traceback
import uuid
from messagequeue import uploadQueueClub
from student import datahandler as studata

tz = pytz.timezone('Asia/Kolkata')
today = datetime.now(tz)


# Create your views here.
@login_required(login_url = '/user/login/')
@group_required("Clubgrp")
def club(request):
    if request.method == 'POST':
        eventId = request.POST['Id']
        if request.POST['action'] == "stopregistration":
            status = eventdataconn.stopRegistration(eventId,False)
        elif request.POST['action'] == "startregistration":
            status = eventdataconn.stopRegistration(eventId , True)
        elif request.POST['action'] == "Deletion":
            status = eventdataconn.deleteEvent(eventId)

    eventsforclub = eventdataconn.getLiveEventforClub(request.user.username , today)
    context = {"events" : eventsforclub}
    return render(request , 'clublanding.html' , context)


@group_not_required("Clubgrp" , "Techgrp")
def clubforid(request , id = 0):
    if(id == 0):
        raise Http404()

    if request.user.is_authenticated:
        if request.method == "POST":
            if request.POST['action'] == 'Subscription':
                studentId = request.POST.get('studentId')
                clubId = request.POST.get('clubId')
                try:
                    dataconn.addStudentSubscription(studentId = studentId , clubId=clubId)
                    stu = studata.getStudent(request.user.username)
                    uploadQueueClub(stu['studentEmail'])
                    print("Subscription successful")
                except:
                    print("Error in adding subcription in view.py of club")

            elif request.POST['action'] == 'Unsubscription':
                studentId = request.POST.get('studentId')
                clubId = request.POST.get('clubId')
                try:
                    dataconn.removeStudentSubscription(studentId = studentId , clubId=clubId)
                    print("unsubscription successful")
                except:
                    traceback.print_exc()
                    print("Error in adding unsubcription in view.py of club")
    
    try:
        clubdata = dataconn.getClub(id)
        if clubdata is None:
            print("None received")
            traceback.print_exc()
            raise Exception

        upcomingEvents = []
        pastEvents = []
        upcomingEvents = eventdataconn.getLiveEventforClub(id,today)
        pastEvents = eventdataconn.getPastEventforClub(id,today)
        context = {"club" : clubdata , "upcoming" : upcomingEvents , "past" : pastEvents}
        return render(request , 'club.html' , context)
    except:
        traceback.print_exc()
        print("error in loading club with id:" + id)
    
    raise Http404

@group_not_required("Clubgrp" , "Techgrp")
def allclubsloaded(request):
    if request.user.is_authenticated: 
        if request.method == 'POST':
            studentId = request.POST['studentId']
            clubId = request.POST['clubId']
            try:
                dataconn.addStudentSubscription(studentId = studentId , clubId=clubId)
                stu = studata.getStudent(request.user.username)
                uploadQueueClub(stu['studentEmail'])
            except:
                traceback.print_exc()
                print("error thrown")
        subscribedClub = dataconn.getSubscribedClubforStudent(request.user.username)
    else:
        subscribedClub = {}
    allclubs = dataconn.getAllClub()
    context = {"allclubs" : allclubs , "subscribed" : subscribedClub}
    if(allclubs is None):
        return HttpResponse("Server Error")

    return render(request , 'clubs.html' , context= context)


@login_required(login_url = '/user/login/')
@group_required("Clubgrp")
def createEvent(request):
    if request.method == 'POST':
        if request.POST['action'] == 'Registration':
            eventName = request.POST['eventName']
            eventLocation = request.POST['eventLocation']
            eventDescription = request.POST['eventDescription']
            eventPosterURL = request.POST['imgUrl']

            eventStartTime = timeconverter(request.POST['eventStartTime'])
            eventEndTime = timeconverter(request.POST['eventEndTime'])
            
            instagramLink = request.POST['instagramLink']
            twitterLink = request.POST['twitterLink']
            linkdenLink = request.POST['linkdenLink']

            id = uuid.uuid1().hex

            eventData = {"eventId" : id , "eventName" : eventName , "eventLocation" : eventLocation , "eventDescription" : eventDescription , 
            "eventPosterURL" : eventPosterURL , "eventStartTime" : eventStartTime , "eventEndTime" : eventEndTime , 
            "instagramLink" : instagramLink , "twitterLink" : twitterLink , "linkdenLink" : linkdenLink , "acceptResponse" : True , 
            "host" : request.user.username }
            
            try:
                status = eventdataconn.createEvent(eventData)
                if status is None:
                    traceback.print_exc()
                    return HttpResponseServerError()
            except:
                traceback.print_exc()
                return HttpResponseServerError()
            
    return render(request , 'createEvent.html')


def timeconverter(unix_timestamp):
    d = datetime.strptime(unix_timestamp , '%Y-%m-%dT%H:%M')
    d.replace(tzinfo=tz)
    return d