from django.db import models

class Renting(models.Model):
    Name = models.CharField(max_length=30 )
    MachineDetails= models.CharField(max_length=200)
    Wages= models.IntegerField(default="0")
    Persons= models.IntegerField(default="0")
    def __str__(self):
        return self.JobTitle


