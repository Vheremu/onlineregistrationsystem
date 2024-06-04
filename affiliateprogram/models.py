from django.db import models
from accounts.models import UserProfileInfo
# Create your models here.
class Add(models.Model):
    addid = models.IntegerField(blank=False,unique=True,primary_key=True)
    adduser = models.ForeignKey(UserProfileInfo,on_delete=models.CASCADE,blank=True)
    addimage = models.ImageField(upload_to='static/addimage',blank=True)
    def __str__(self):
        return self.adduser.user.username