from django.db import models
from accounts.models import User
from datetime import datetime

class Renting(models.Model):
    Name = models.CharField(max_length=30 )
    MachineDetails= models.CharField(max_length=200)
    Price= models.IntegerField(default="0")
    Contact=models.IntegerField(default="0")
    user_id=models.ForeignKey(User , to_field='id', on_delete=models.CASCADE, unique=True,blank=True, null=True)
    rentimage=models.ImageField(upload_to="RentMachine/thumb-img", blank=True, null=True,default="" )
    BookedStatus = models.BooleanField("BookedStatus", default=False)
    date = models.DateField(, auto_now=False, blank=True) 


    def __str__(self):
        return self.Name


