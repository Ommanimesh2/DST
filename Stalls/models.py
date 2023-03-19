from django.db import models
from accounts.models import User

class Stalls(models.Model):
    Stalltopic = models.CharField(max_length=30 )
    Date= models.DateField(max_length=200)
    Location= models.CharField(default="0",max_length=100)
    Time= models.TimeField(default="0")
    Phoneno=models.IntegerField()
    username=models.ForeignKey(User , to_field='username', on_delete=models.CASCADE, unique=True,blank=True, null=True)
    def __str__(self):
        return self.Stalltopic

