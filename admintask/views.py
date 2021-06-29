from django.shortcuts import render , HttpResponse
from django.contrib.auth.decorators import login_required
from grpcheckerview import group_required
from club import datahandler as dataconn
# Create your views here.

@login_required(login_url = '/user/login/')
@group_required("Techgrp")
def adminLanding(request):
    if request.method == 'POST':
        if request.POST['action'] == 'Deletion':
            id = request.POST.get('ID')
            dataconn.deleteClub(id)

    clubs = dataconn.getAllClub()
    context = {"clubs" : clubs}
    return render(request , 'adminlanding.html' , context)
    
@login_required(login_url = '/user/login/')
@group_required("Techgrp")
def createClub(request):
    if request.method == 'POST':
        if request.POST['action'] == "RegisterClub":
            clubname = request.POST.get('clubName')
            clubemail = request.POST.get('clubEmail')
            clubDescription = request.POST.get('clubDescription')
            clubImgUrl = request.POST.get('imgUrl')
            ClubData = {"clubName" : clubname , "clubEmail" : clubemail , "clubDescription" : clubDescription , "clubImgUrl" : clubImgUrl}
            ClubData["discordLink"] = ""
            ClubData["instaLink"] = ""
            ClubData["linkedinLink"]  = ""
            ClubData["telegramLink"] = ""
            ClubData["twitterLink"] = ""
            ClubData["whatsappLink"] =  ""
            ClubData["youtubeLink"] = ""
            password = dataconn.createClub(ClubData)
            if password is None:
                return render(request , 'createClub.html')    
            context = {"password" : password}
            return render(request , 'createClub.html' , context)

    return render(request , 'createClub.html')