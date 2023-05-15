from django.db import models
from accounts.models import User
from datetime import datetime


class Renting(models.Model):
    Name = models.CharField(max_length=30 )
    MachineDetails= models.CharField(max_length=200)
    Price= models.IntegerField(default="0")
    Contact=models.IntegerField(default="0")
    rentimage=models.CharField(max_length=1000, blank=True, default="https://firebasestorage.googleapis.com/v0/b/bhoomirent-df650.appspot.com/o/rn_image_picker_lib_temp_2512f23f-19ab-4ea7-9a4a-48ae50b9de9c.jpg?alt=media&token=7293eb19-9505-4910-8eb9-ee58d2f14ae5")
    BookedStatus = models.BooleanField("BookedStatus", default=False)
    date = models.DateField(auto_now=False, blank=True) 
    def __str__(self):
        return self.Name


class Orders(models.Model):
    PAYEMENT_CHOICES=(
        ('COD', "Cash on Delivery"),
        ('Online', "Online Payement"),
    )
    machine_id=models.IntegerField(default="0")
    date = models.DateField( auto_now=False, blank=True) 
    placed_at=models.DateField(auto_now=True, blank=True  )
    user_id=models.IntegerField(default="0")
    payement_status=models.BooleanField("payement_status", default=False)
    payement_mode = models.CharField(max_length=30, choices=PAYEMENT_CHOICES)
    def __str__(self):
        return self.payement_mode    
    
class query(models.Model):
    machine_name=models.CharField(max_length=100)
    message=models.CharField(max_length=200)
    query_img=models.CharField(max_length=1000,blank=False, default="https://firebasestorage.googleapis.com/v0/b/bhoomirent-df650.appspot.com/o/rn_image_picker_lib_temp_2512f23f-19ab-4ea7-9a4a-48ae50b9de9c.jpg?alt=media&token=7293eb19-9505-4910-8eb9-ee58d2f14ae5")
    user_id=models.IntegerField(default="0")
    
    def __str__(self):
        return self.machine_name