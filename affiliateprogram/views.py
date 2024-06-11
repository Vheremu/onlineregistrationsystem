from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from imagecode import printpromo,printpromocode,a1
from accounts.models import UserProfileInfo
from .models import Add,Promocode,Token,Invitation
from configcode import getid,getid1
import time,datetime
# Create your views here.
@login_required
def adds(request):
    print(request.POST)
    adds=Add.objects.filter(adduser=2)
    my_dict = {'adds':adds}
    return render(request,'affiliateprogram/adds.html',context=my_dict)
@login_required
def confirmgetadd(request):
    addid=request.POST.get('addid')
    add=Add.objects.get(addid=addid)
    image=printpromo(add.addimage)
    my_dict = {'add':add,'image':image}
    return render(request,'affiliateprogram/confirmgetadd.html',context=my_dict)
@login_required
def myadds(request):
    user=request.user
    user=UserProfileInfo.objects.get(user=user)
    if request.POST:
        addid=request.POST.get('addid')
        add=Add.objects.get(addid=addid)
        promocode=getid()
        promocode=Promocode.objects.create(promocodeuser=user,promocode=str(user)+str(promocode))
        image=printpromocode(add.addimage,promocode.promocode)
        image=image.save('static/adds/promocode'+promocode.promocode+'.png')
        Add.objects.create(adduser=user,addimage='static/adds/promocode'+promocode.promocode+'.png')
    
    adds=Add.objects.filter(adduser=user)
    my_dict = {'adds':adds}
    return render(request,'affiliateprogram/myadds.html',context=my_dict)
@login_required
def generateinvitationletter(request):
    user=request.user
    user=UserProfileInfo.objects.get(user=user)
    generate=request.POST.get('generate')
    if generate:
        print('helo world')
        firstname=request.POST.get('inviterfirstname')
        surname=request.POST.get('invitersurname')
        invitee=request.POST.get('firstname')
        inviteesurname=request.POST.get('surname')
        token='aacaffiliatetoken'+getid1()
        date=datetime.datetime.now()
        token=Token.objects.create(tokenuser=user,token=token)
        date=datetime.datetime.now()
        image=a1(firstname=firstname,surname=surname,invitee=invitee,inviteesurname=inviteesurname,token=token.token)
        image=image.save('static/invitationletters/invitation'+token.token+'.png')
        invitation=Invitation.objects.create(invitationinvitee=invitee,invitationinviteesurname=inviteesurname,invitationuser=user,invitationstatus='pending',invitationimage='static/invitationletters/invitation'+token.token+'.png')
        my_dict = {'invitation':invitation}
        return render(request,'affiliateprogram/generateinvitationletter.html',context=my_dict)
    my_dict = {}
    return render(request,'affiliateprogram/generateinvitationletter.html',context=my_dict)
@login_required
def account(request):
    user=request.user
    user=UserProfileInfo.objects.get(user=user)
    invitation=Invitation.objects.filter(invitationuser=user)
    my_dict = {'invitation':invitation}
    return render(request,'affiliateprogram/account.html',context=my_dict)
