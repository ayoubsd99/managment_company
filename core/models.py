from  django.db import models
# Create your models here.


class BaseModel(models.Model):
    reference=models.CharField(max_length=50)
    created_at=models.DateTimeField(auto_now_add=True,auto_now=False)
    updated_at=models.DateTimeField(auto_now_add=False,auto_now=True)
    deleted=models.BooleanField(default=False)

    def __str__(self):

        return self.reference

    class Meta :   

        abstract : True

class AppPermission(models.Model):
    label=models.CharField(max_length=50,unique=True)

    def __str__(self):

        return self.label        

class Country(models.Model):
    
    label = models.CharField(max_length=50,unique=True)

    def __str__(self):

        return self.label

class City(models.Model):

    label = models.CharField(max_length=50,unique=True)


    def __str__(self):
        return self.label



