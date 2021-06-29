from django import template
from admintask.models import registration
from student.models import Student
from event.models import Event
from club import datahandler as  clubdata
import traceback

register = template.Library() 
@register.filter(name='is_registered') 
def is_registered(user, EventId):
    try:
        id = user
        stu = id
        eve = EventId
        try:
            result = registration.objects.get(eventId=eve ,studentId=stu)
            return False
        except:
            traceback.print_exc()
            return True
    except:
        return True

@register.filter(name = "getClub")
def clubName(clubId):
    try:
        club = clubdata.getClub(clubId)
        return club['clubName']
    except:
        traceback.print_exc()
        return "Error"