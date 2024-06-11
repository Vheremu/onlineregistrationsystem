from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from data.models import Registration,Pop,Feedback,Contact
from accounts.models import UserProfileInfo
from affiliateprogram.models import Promocode
import time,datetime
def index(request):
    my_dict = {}
    return render(request,'onlineregistration/index.html',context=my_dict)
@login_required
def feedback(request):
    
    user=request.user
    user= UserProfileInfo.objects.get(user=user)
    website=request.POST.get('website')
    comment=request.POST.get('comment')
    if website:
        
        feedback=Feedback.objects.create(feedbackuser=user,feedbackrating=website,feedbackcomment=comment)
        my_dict = {'submit':'submit'}
        return render(request,'onlineregistration/feedback.html',context=my_dict)
    my_dict = {}
    return render(request,'onlineregistration/feedback.html',context=my_dict)
def contactus(request):
    print(request.POST)
    fullname=request.POST.get('fullname')
    companyname=request.POST.get('companyname')
    numemployees=request.POST.get('numemployees')
    business=request.POST.get('business')
    if fullname:
        contact=Contact.objects.create(contactname=fullname,contactcompany=companyname,contactcompanyemployees=numemployees,contactbusiness=business)
        my_dict = {'contact':contact}
        return render(request,'onlineregistration/contactus.html',context=my_dict)
    my_dict = {}
    return render(request,'onlineregistration/contactus.html',context=my_dict)
@login_required
def admissions(request):
    my_dict = {}
    return render(request,'onlineregistration/admissions.html',context=my_dict)
@login_required
def makepayment(request):
    my_dict = {}
    return render(request,'onlineregistration/makepayment.html',context=my_dict)
def aboutus(request):
    my_dict = {}
    return render(request,'onlineregistration/aboutus.html',context=my_dict)
@login_required
def uploadproofofpayment(request):
    user=request.user
    user= UserProfileInfo.objects.get(user=user)
    myregistrations=Registration.objects.filter(user=user)
    message=''
    if request.POST:
        try:
            print(request.POST)
            regid=request.POST.get('registration')
            registration=Registration.objects.get(registrationid=regid)
            pop=request.FILES['pop']
            Pop.objects.create(registration=registration,pop=pop,popuser=user)
            message='Succesfuly Uploaded Pop'
        except:
            print('error occured')
            message='Failed to Upload Pop'
            
    pops=Pop.objects.filter(popuser=user)
    print('Helo World')
    my_dict = {'myregistrations':myregistrations,'pops':pops,'message':message}
    return render(request,'onlineregistration/uploadproofofpayment.html',context=my_dict)
@login_required
def paymentdetails(request):
    print(request.POST)
    promocode=request.POST.get('promocode')
    if promocode:
        promo=request.POST.get('promo')
        try:
            promocode=Promocode.objects.get(promocode=promocode)
            print('valid promocode')
            if promo=='dayscholar':
                print('day scholar')
                dayscholar=1
                my_dict = {'dayscholar':dayscholar,'promocode':promocode}
                return render(request,'onlineregistration/paymentdetails.html',context=my_dict)
            else:
                print('boarder')
                boarder=1
                my_dict = {'boarder':boarder,'promocode':promocode}
                return render(request,'onlineregistration/paymentdetails.html',context=my_dict)
        except:
            print('invalid promocode')
        
    my_dict = {}
    return render(request,'onlineregistration/paymentdetails.html',context=my_dict)
@login_required
def viewregistration(request):
    ids=request.POST.get('id')
    registration=Registration.objects.get(registrationid=ids)
    
    print(request.POST)
    my_dict = {'registration':registration}
    return render(request,'onlineregistration/viewregistration.html',context=my_dict)
@login_required
def easyregistration(request):
    easyregistration=request.POST.get('easyregistration')
   
    course=request.POST.get('course')
    parentname=request.POST.get('parentname')
    parentsurname=request.POST.get('parentsurname')
    parentemail=request.POST.get('parentemail')
    parentphonenumber=request.POST.get('parentphonenumber')
    studentname=request.POST.get('studentname')
    studentsurname=request.POST.get('studentsurname')
    studentsex=request.POST.get('studentsex')
    form=request.POST.get('form')
    zimsec=0
    user=request.user
    user= UserProfileInfo.objects.get(user=user)
    myregistrations=Registration.objects.filter(user=user)
    if easyregistration:
        if parentname:
            if parentsurname:
                if course:
                    if parentemail:
                        if parentphonenumber:
                            if studentname:
                                if studentsurname:
                                    if studentsex:
                                        if form:
                                            user=request.user
                                            user= UserProfileInfo.objects.get(user=user)
                                            Registration.objects.create(status='pending',user=user,course=course,parentname=parentname,parentsurname=parentsurname,parentemail=parentemail,parentphonenumber=parentphonenumber,studentname=studentname,studentsurname=studentsurname,registrationdate=datetime.datetime.now(),studentsex=studentsex,form=form)
                                            message='Registration For '+studentname+' Successful!'
                                            my_dict = {'message':message,'myregistrations':myregistrations}
                                            return render(request,'onlineregistration/onlineregistration.html',context=my_dict)
                                        else:
                                            message='Please Fill In All The Required Information!'
                                            my_dict = {'message':message,'myregistrations':myregistrations}
                                            return render(request,'onlineregistration/onlineregistration.html',context=my_dict)
                                    else:
                                        message='Please Fill In All The Required Information!'
                                        my_dict = {'message':message,'myregistrations':myregistrations}
                                        return render(request,'onlineregistration/onlineregistration.html',context=my_dict)
                                else:
                                    message='Please Fill In All The Required Information!'
                                    my_dict = {'message':message,'myregistrations':myregistrations}
                                    return render(request,'onlineregistration/onlineregistration.html',context=my_dict)
                            else:
                                message='Please Fill In All The Required Information!'
                                my_dict = {'message':message,'myregistrations':myregistrations}
                                return render(request,'onlineregistration/onlineregistration.html',context=my_dict)
                        else:
                            message='Please Fill In All The Required Information!'
                            my_dict = {'message':message,'myregistrations':myregistrations}
                            return render(request,'onlineregistration/onlineregistration.html',context=my_dict)
                            
                    else:
                        message='Please Fill In All The Required Information!'
                        my_dict = {'message':message,'myregistrations':myregistrations}
                        return render(request,'onlineregistration/onlineregistration.html',context=my_dict)
                else:
                    message='Please Fill In All The Required Information!'
                    my_dict = {'message':message,'myregistrations':myregistrations}
                    return render(request,'onlineregistration/onlineregistration.html',context=my_dict)
            else:
                message='Please Fill In All The Required Information'
                my_dict = {'message':message,'myregistrations':myregistrations}
                return render(request,'onlineregistration/onlineregistration.html',context=my_dict)
        else:
            message='Please Fill In All The Required Information!'
            my_dict = {'message':message,'myregistrations':myregistrations}
            return render(request,'onlineregistration/onlineregistration.html',context=my_dict)
        
        my_dict = {'myregistrations':myregistrations}
        return render(request,'onlineregistration/onlineregistration.html',context=my_dict)
    campridge=0
    my_dict = {'myregistrations':myregistrations}
    return render(request,'onlineregistration/onlineregistration.html',context=my_dict)
def onlineregistration(request):
    print(request.POST)
    onlineregistration=request.POST.get('onlineregistration')
    easyregistration=request.POST.get('easyregistration')
        

    if easyregistration:
        print(easyregistration+'easy registration')
        course=request.POST.get('course')
        parentname=request.POST.get('parentname')
        parentsurname=request.POST.get('parentsurname')
        parentemail=request.POST.get('parentemail')
        parentphonenumber=request.POST.get('parentphonenumber')
        studentname=request.POST.get('studentname')
        studentsurname=request.POST.get('studentsurname')
        studentsex=request.POST.get('studentsex')
        form=request.POST.get('form')
        
        
        print(parentname+parentsurname)
        zimsec=0
        campridge=0
        if parentname:
            if parentsurname:
                if course:
                    if parentemail:
                        if parentphonenumber:
                            if studentname:
                                if studentsurname:
                                    if studentsex:
                                        if form:
                                            user=request.user
                                            user= UserProfileInfo.objects.get(user=user)
                                            Registration.objects.create(user=user,course=course,parentname=parentname,parentsurname=parentsurname,parentemail=parentemail,parentphonenumber=parentphonenumber,studentname=studentname,studentsurname=studentsurname,registrationdate=datetime.datetime.now(),studentsex=studentsex,form=form)
                                            message='Registration For '+studentname+' Successful!'
                                            my_dict = {'message':message}
                                            return render(request,'onlineregistration/onlineregistration.html',context=my_dict)
                                        else:
                                            message='Please Fill In All The Required Information!'
                                            my_dict = {'message':message}
                                            return render(request,'onlineregistration/onlineregistration.html',context=my_dict)
                                    else:
                                        message='Please Fill In All The Required Information!'
                                        my_dict = {'message':message}
                                        return render(request,'onlineregistration/onlineregistration.html',context=my_dict)
                                else:
                                    message='Please Fill In All The Required Information!'
                                    my_dict = {'message':message}
                                    return render(request,'onlineregistration/onlineregistration.html',context=my_dict)
                            else:
                                message='Please Fill In All The Required Information!'
                                my_dict = {'message':message}
                                return render(request,'onlineregistration/onlineregistration.html',context=my_dict)
                        else:
                            message='Please Fill In All The Required Information!'
                            my_dict = {'message':message}
                            return render(request,'onlineregistration/onlineregistration.html',context=my_dict)
                            
                    else:
                        message='Please Fill In All The Required Information!'
                        my_dict = {'message':message}
                        return render(request,'onlineregistration/onlineregistration.html',context=my_dict)
                else:
                    message='Please Fill In All The Required Information!'
                    my_dict = {'message':message}
                    return render(request,'onlineregistration/onlineregistration.html',context=my_dict)
            else:
                message='Please Fill In All The Required Information'
                my_dict = {message}
                return render(request,'onlineregistration/onlineregistration.html',context=my_dict)
        else:
            message='Please Fill In All The Required Information!'
            my_dict = {'message':message}
            return render(request,'onlineregistration/onlineregistration.html',context=my_dict)
        
        my_dict = {}
        return render(request,'onlineregistration/onlineregistration.html',context=my_dict)
    if onlineregistration:
        print(onlineregistration+'online registration')
        my_dict = {}
        return render(request,'onlineregistration/onlineregistration.html',context=my_dict)
    my_dict = {}
    return render(request,'onlineregistration/onlineregistration1.html',context=my_dict)