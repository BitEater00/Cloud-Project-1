from pymongo import MongoClient
from event.models import Event
from club.models import Club
from student.models import Student
from admintask.models import subscription
from admintask.models import registration
from student import datahandler as studata
import traceback

client = MongoClient("")
db = client.get_database("CloudProject")
conn = db.Events


def createEvent(eventData):
    try:        
        conn.insert_one(eventData)    
        event = Event(eventId=eventData['eventId'])
        event.save()
    except:
        traceback.print_exc()
        return None
    return True


def deleteEvent(id):
    try:
        conn.delete_one({"eventId" : id})
        Event.objects.filter(eventId = id).delete()
        try:
            registration.objects.all().filter(eventId=eventId).delete()
        except:
            traceback.print_exc()
            print("No registration")
    except:
        return None
    return True

def deleteEventforClub(clubId):
    try:
        events = getEventForClub(clubId)
        eventIds = [ sub['eventId'] for sub in events ]
        conn.delete_many({"host" : clubId})
        Event.objects.filter("eventId" in eventIds).delete()
    except:
        return None
    return True

def getAllEvent():
    try:
        return conn.find()
    except:
        return None

def getAllLiveEvent(today):
    try:
        return conn.find({ "eventEndTime" : { '$gte' : today} })
    except:
        traceback.print_exc()
        return None

def getEvent(id):
    try:
        return conn.find_one({"eventId" : id})
    except:
        return None


def getSubscribedEventforStudent(studentId , today):
    try:
        events = []
        clubIds = subscription.objects.all().filter(studentId = studentId).values_list('clubId', flat=True)
        for x in clubIds:
            print("Event printing")
            print(getLiveEventforClub(x,today))
            events.append(getLiveEventforClub(x,today))
        print(events)
        return events
    except:
        print("Error in getSubcribedEventforStudent")
        traceback.print_exc()
        return None


def getRegisteredEventforStudent(studentId):
    events = []
    eventIds = registration.objects.all().filter(studentId = studentId).values_list('eventId', flat=True)
    for x in eventIds:
        events.append(getEvent(x))
    return events


def getEventForClub(clubId):
    return conn.find({"host" : clubId})

def getLiveEventforClub(clubId , today):
    return conn.find({ "$and": [ {"host" : clubId} , { "eventEndTime" : { '$gte' : today} } ]} )

def getPastEventforClub(clubId , today):
    return conn.find({ "$and": [ {"host" : clubId} , { "eventEndTime" : { '$lte' : today} } ]} )

def removeStudentRegistration(studentId , eventId):
    registration.objects.all().filter(eventId = eventId , studentId=studentId).delete()


def addStudentRegistration(studentId , eventId):
    subs = registration(studentId=studentId, eventId= eventId)
    subs.save()

def stopRegistration(eventId , value):
    try:
        query = {"eventId" : eventId}
        update = {"$set" : {"acceptResponse" : value}}
        conn.update_one(query , update)
    except:
        traceback.print_exc()
        return None
    return True

def updateEvent(id , updatedData):
    try:  
        query = {"eventId" : id}
        update = {"$set": updatedData}
        conn.update_one(query , update)
    except:
        return None
    return True

def getParticipant(id):
    try:
        student = []
        studentIds = registration.objects.all().filter(eventId= id).values_list('studentId', flat=True)
        for x in studentIds:
            student.append(studata.getStudent(x))
        return student
    except:
        traceback.print_exc()
        return None