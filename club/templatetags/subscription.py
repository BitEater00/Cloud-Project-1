from django import template
from admintask.models import subscription
from student.models import Student
from club.models import Club
import traceback

register = template.Library() 
@register.filter(name='isStudentSubscribed') 
def isStudentSubscribed(user, ClubId):
    try:
        id = user
        stu = id
        clu = ClubId
        try:
            result = subscription.objects.get(clubId=clu , studentId=stu)
            return False
        except:
            return True
    except:
        traceback.print_exc()
        print("error in subscription")
        return True