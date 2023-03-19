from django.db import models
from accounts.models import User

class Jobs(models.Model):
    JobTitle = models.CharField(max_length=30 )
    days= models.CharField(max_length=200)
    price= models.IntegerField(default="0")
    workers= models.IntegerField(default="0")
    contact= models.IntegerField(default="0")
    username=models.ForeignKey(User , to_field='username', on_delete=models.CASCADE, unique=True,blank=True, null=True)
    def __str__(self):
        return self.JobTitle

