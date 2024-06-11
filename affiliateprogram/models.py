from django.db import models
from accounts.models import UserProfileInfo
# Create your models here.
class Add(models.Model):
    addid = models.IntegerField(blank=False,unique=True,primary_key=True)
    adduser = models.ForeignKey(UserProfileInfo,on_delete=models.CASCADE,blank=True)
    addimage = models.ImageField(upload_to='static/addimage',blank=True)
    def __str__(self):
        return self.adduser.user.username
class Promocode(models.Model):
    promocodeid = models.IntegerField(blank=False,unique=True,primary_key=True)
    promocodeuser = models.ForeignKey(UserProfileInfo,on_delete=models.CASCADE,blank=True)
    promocode = models.CharField(blank=False,max_length=100,unique=False)
    def __str__(self):
        return self.adduser.user.username
class Token(models.Model):
    tokenid = models.IntegerField(blank=False,unique=True,primary_key=True)
    tokenuser = models.ForeignKey(UserProfileInfo,on_delete=models.CASCADE,blank=True)
    token = models.CharField(blank=False,max_length=100,unique=False)
    def __str__(self):
        return self.tokenuser.user.username
class Invitation(models.Model):
    invitationid = models.IntegerField(blank=False,unique=True,primary_key=True)
    invitationuser = models.ForeignKey(UserProfileInfo,on_delete=models.CASCADE,blank=True)
    invitationimage = models.ImageField(upload_to='static/invitationletters',blank=True)
    invitationinvitee = models.CharField(default='',blank=False,max_length=100,unique=False)
    invitationinviteesurname = models.CharField(default='',blank=False,max_length=100,unique=False)
    invitationstatus = models.CharField(blank=False,max_length=100,unique=False)
    def __str__(self):
        return self.invitationuser.user.username