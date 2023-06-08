from django.db import models
from accounts.models import User
from datetime import datetime
import uuid
# from django.contrib.gis.db import models



KVK_CHOICES=(
("Rajat Agricultural works","Rajat Agricultural works"),
("Rudraksh Farmtrac Roorkee","Rudraksh Farmtrac Roorkee"),
("Agri Service Center","Agri Service Center")
)

class KVKs(models.Model):
    Name_KVK=models.CharField(choices=KVK_CHOICES ,max_length=200)
    Address=models.CharField(max_length=300)
    Contact_KVK=models.IntegerField()
    Name_of_Head=models.CharField(max_length=100)
    coordinate_x =  models.DecimalField(max_digits=80, decimal_places=20)
    coordinate_y=models.DecimalField(max_digits=80, decimal_places=20)
    def __str__(self):
        return self.Name_KVK
    

class Renting(models.Model):
    KVK = models.ForeignKey(KVKs, on_delete=models.PROTECT)
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
    start_date = models.DateField( auto_now=False, blank=True) 
    end_date = models.DateField( auto_now=False, blank=True, default="2023-06-04")
    placed_at=models.DateField(auto_now=True, blank=True  )
    user_id=models.IntegerField(default="0")
    payement_status=models.BooleanField("payement_status", default=False)
    payement_mode = models.CharField(max_length=30, choices=PAYEMENT_CHOICES)
    def __str__(self):
        return self.payement_mode    
    
class query(models.Model):
    name=models.CharField(max_length=100)
    email = models.CharField(max_length=80,default="fdjgk")
    subject = models.CharField(max_length=100,default="fdjgk")
    message=models.CharField(max_length=500,default="fdjgk")
    user_id=models.IntegerField(default="0")
    
    def __str__(self):
        return self.name
    
class FourImages(models.Model):
    user_id=models.IntegerField(default="0")
    first_img=models.CharField(max_length=1000, blank=True, default="https://firebasestorage.googleapis.com/v0/b/bhoomirent-df650.appspot.com/o/rn_image_picker_lib_temp_2512f23f-19ab-4ea7-9a4a-48ae50b9de9c.jpg?alt=media&token=7293eb19-9505-4910-8eb9-ee58d2f14ae5")
    second_img=models.CharField(max_length=1000, blank=True, default="https://firebasestorage.googleapis.com/v0/b/bhoomirent-df650.appspot.com/o/rn_image_picker_lib_temp_2512f23f-19ab-4ea7-9a4a-48ae50b9de9c.jpg?alt=media&token=7293eb19-9505-4910-8eb9-ee58d2f14ae5")
    third_img=models.CharField(max_length=1000, blank=True, default="https://firebasestorage.googleapis.com/v0/b/bhoomirent-df650.appspot.com/o/rn_image_picker_lib_temp_2512f23f-19ab-4ea7-9a4a-48ae50b9de9c.jpg?alt=media&token=7293eb19-9505-4910-8eb9-ee58d2f14ae5")
    fourth_img=models.CharField(max_length=1000, blank=True, default="https://firebasestorage.googleapis.com/v0/b/bhoomirent-df650.appspot.com/o/rn_image_picker_lib_temp_2512f23f-19ab-4ea7-9a4a-48ae50b9de9c.jpg?alt=media&token=7293eb19-9505-4910-8eb9-ee58d2f14ae5")
    def __str__(self):
        return self.user_id
    