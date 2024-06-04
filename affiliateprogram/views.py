from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from imagecode import printpromo
from .models import Add
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
    image.save
    my_dict = {'add':add,'image':image}
    return render(request,'affiliateprogram/confirmgetadd.html',context=my_dict)
@login_required
def myadds(request):
    my_dict = {}
    return render(request,'affiliateprogram/myadds.html',context=my_dict)
@login_required
def account(request):
    my_dict = {}
    return render(request,'affiliateprogram/account.html',context=my_dict)
