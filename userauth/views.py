from django.shortcuts import render , HttpResponse , redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login , logout
from student import datahandler as studata
from club import datahandler as clubdata
from django.http import *
import traceback
import pyrebase

#enter the firebase config api keys
firebaseConfig = {
}

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()

def loginuser(request):
    if request.user.is_authenticated:
        try:
            return redirect(request.GET.get('next'))
        except:
            traceback.print_exc()
            return redirect("/")

    if request.method == 'POST':
        email = request.POST['username']
        password = request.POST['password']
        try:
            urltoredirect = request.POST['redirecturl']
        except:
            urltoredirect = None
        try:
            user = auth.sign_in_with_email_and_password(email , password)
            user = authenticate(username=user['localId'], password="deZE%KYzH5jVBbHN")
            if user is not None:
                login(request, user)
                if not(urltoredirect is None):
                    return redirect(urltoredirect)
                else:
                    if user.groups.filter(name = "Studentgrp").exists():
                        return redirect("/student")
                    elif user.groups.filter(name = "Techgrp").exists():
                        return redirect("/admin")
                    else:
                        return redirect("/club")
            else:
                raise Exception
        except:
            traceback.print_exc()
            return render(request, 'login.html' , {"alert" : 1})
    
    return render(request, 'login.html' , {"alert" : 0})


def signup(request):
    if request.user.is_authenticated:
        try:
            return redirect(request.GET.get('next'))
        except:
            return redirect("/")

    if request.method == 'POST':
        studentId = request.POST['id']
        studentName = request.POST['name']
        studentEmail = request.POST['email']
        password = request.POST['password']
        studentData = {"studentId" : studentId , "studentName" : studentName ,"studentEmail" : studentEmail}
        status = studata.createStudent(studentData,password)
        if status is None:
            return HttpResponse(status = 500)
        else:
            return render(request , 'thankyou.html')

    return render(request , 'signup.html') 

def logoutuser(request):
    if request.user.is_authenticated:
        logout(request)
        return render(request , 'logout.html')
    else:
        return redirect('/user/login/')


@login_required(login_url = '/user/login/')
def changepassword(request):
    try:
        userEmail = request.user.email
        auth.send_password_reset_email(userEmail)
        logout(request)
        return render(request , 'changepassword.html')
    except:
        traceback.print_exc()
        return HttpResponseServerError()
    

@login_required(login_url = '/user/login/')
def loadprofile(request):
    if request.user.groups.filter(name = "Studentgrp").exists():
        id = request.user.username
        studentData = studata.getStudent(id)
        if studentData is None:
            raise Http404()
        
        context = {"studentData" : studentData}
        return render(request , 'studentprofile.html' , context)
    
    elif request.user.groups.filter(name = "Clubgrp").exists():
        if request.method == 'POST':
            if request.POST['action'] == "Update":
                clubname = request.POST.get('clubName')
                clubemail = request.POST.get('clubEmail')
                clubDescription = request.POST.get('clubDescription')
                clubImgUrl = request.POST.get('imgUrl')
                ClubData = {"clubName" : clubname , "clubEmail" : clubemail , "clubDescription" : clubDescription , "clubImgUrl" : clubImgUrl}
                ClubData["discordLink"] =  request.POST.get('discordLink')
                ClubData["instaLink"] =  request.POST.get('instaLink')
                ClubData["linkedinLink"]  =  request.POST.get('linkedinLink')
                ClubData["telegramLink"] =  request.POST.get('telegramLink')
                ClubData["twitterLink"] =  request.POST.get('twitterLink')
                ClubData["whatsappLink"] =   request.POST.get('whatsappLink')
                ClubData["youtubeLink"] =  request.POST.get('youtubeLink')

                try:
                    clubdata.updateClub(request.user.username , ClubData)
                except:
                    traceback.print_exc()
                    return HttpResponseServerError()

        id = request.user.username
        data = clubdata.getClub(id)
        if data is None:
            raise Http404()
        
        context = {"club" : data}
        return render(request , 'clubprofile.html' , context)

    elif request.user.groups.filter(name = "Techgrp").exists():
        return redirect("/admin")
    
    else:
        return HttpResponseForbidden()