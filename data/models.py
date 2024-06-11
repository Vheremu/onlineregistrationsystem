from django.db import models
from accounts.models import UserProfileInfo
# Create your models here.
class Registration(models.Model):
    registrationid = models.IntegerField(blank=False,unique=True,primary_key=True)
    user = models.ForeignKey(UserProfileInfo,on_delete=models.CASCADE,blank=True)
    course = models.CharField(blank=False,max_length=100,unique=False)
    status = models.CharField(blank=True,max_length=100,unique=False)
    parentname = models.CharField(blank=False,max_length=100,unique=False)
    parentsurname = models.CharField(blank=False,max_length=100,unique=False)
    parentemail = models.CharField(blank=False,max_length=100,unique=False)
    parentphonenumber = models.CharField(blank=False,max_length=100,unique=False)
    studentname = models.CharField(blank=False,max_length=100,unique=False)
    studentsurname = models.CharField(blank=False,max_length=100,unique=False)
    studentsex = models.CharField(blank=False,max_length=100,unique=False)
    form = models.CharField(blank=False,max_length=100,unique=False)
    registrationdate= models.DateTimeField(verbose_name='startdate',null=False)
    def __str__(self):
        return self.user.user.username
class Pop(models.Model):
    popid = models.IntegerField(blank=False,unique=True,primary_key=True)
    popuser = models.ForeignKey(UserProfileInfo,on_delete=models.CASCADE,blank=True)
    registration = models.ForeignKey(Registration,on_delete=models.CASCADE,blank=True)
    pop = models.ImageField(upload_to='static/pop',blank=True)
    def __str__(self):
        return self.popuser.user.username
class Admission(models.Model):
    admissionid = models.IntegerField(blank=False,unique=True,primary_key=True)
    admissionuser = models.ForeignKey(UserProfileInfo,on_delete=models.CASCADE,blank=True)
    registration = models.ForeignKey(Registration,on_delete=models.CASCADE,blank=True)
    def __str__(self):
        return self.admissionuser.user.username
class Feedback(models.Model):
    feedbackid = models.IntegerField(blank=False,unique=True,primary_key=True)
    feedbackuser = models.ForeignKey(UserProfileInfo,on_delete=models.CASCADE,blank=True)
    feedbackrating = models.CharField(blank=False,max_length=100,unique=False)
    feedbackcomment= models.CharField(blank=False,max_length=100,unique=False)
    def __str__(self):
        return self.feedbackuser.user.username
class Contact(models.Model):
    contactid = models.IntegerField(blank=False,unique=True,primary_key=True)
    contactname = models.CharField(blank=False,max_length=100,unique=False)
    contactcompany = models.CharField(blank=False,max_length=100,unique=False)
    contactcompanyemployees = models.CharField(blank=False,max_length=100,unique=False)
    contactbusiness = models.CharField(blank=False,max_length=100,unique=False)
    def __str__(self):
        return self.contactname