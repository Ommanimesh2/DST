from django.db import models

class Jobs(models.Model):
    JobTitle = models.CharField(max_length=30 )
    Description= models.CharField(max_length=200)
    Wages= models.IntegerField(default="0")
    Persons= models.IntegerField(default="0")
    def __str__(self):
        return self.JobTitle


