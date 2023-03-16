from django.db import models
from accounts.models import User

class Jobs(models.Model):
    JobTitle = models.CharField(max_length=30 )
    Description= models.CharField(max_length=200)
    Wages= models.IntegerField(default="0")
    Persons= models.IntegerField(default="0")
    username=models.ForeignKey(User , to_field='username', on_delete=models.CASCADE, unique=True,blank=True, null=True)
    def __str__(self):
        return self.JobTitle

