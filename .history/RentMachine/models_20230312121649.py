from django.db import models

class Renting(models.Model):
    Name = models.CharField(max_length=30 )
    MachineDetails= models.CharField(max_length=200)
    Price= models.IntegerField(default="0")
    Contact=models.IntegerField(default="0")
    # Image=models.ImageField()
    def __str__(self):
        return self.Name


