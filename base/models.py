from django.db import models

# Create your models here.
from django.db import models


# Create your models here.
class Student(models.Model):
    image = models.ImageField(null=True,blank=True,default='/placeholder.png')
    id = models.BigAutoField(primary_key=True)
    sName = models.CharField(max_length=20)
    age = models.FloatField()


    def __str__(self):
        return self.sName