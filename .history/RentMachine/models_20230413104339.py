from django.db import models
from accounts.models import User

class Renting(models.Model):
    Name = models.CharField(max_length=30 )
    MachineDetails= models.CharField(max_length=200)
    Price= models.IntegerField(default="0")
    Contact=models.IntegerField(default="0")
    user_id=models.ForeignKey(User , to_field='user_id', on_delete=models.CASCADE, unique=True,blank=True, null=True)
    rentimage=models.ImageField(upload_to="RentMachine/thumb-img", blank=True, null=True)
    
   
    def __str__(self):
        return self.Name


