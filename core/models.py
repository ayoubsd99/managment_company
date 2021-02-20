from  django.db import models
# Create your models here.

from django.db import models

class BaseModel(models.Model):
    reference = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)
    deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.reference

    class Meta :
        abstract = True

class AppPermission(models.Model):
    label = models.CharField(max_length=50,unique=True)

    def __str__(self):
        return self.label

class Country(models.Model):
    label = models.CharField(max_length=50,unique=True)

    def __str__(self):
        return self.label

class City(models.Model):
    label = models.CharField(max_length=100,unique=True)
    coutry = models.ForeignKey("core.Country",on_delete=models.CASCADE,default='Moroco')

    def __str__(self):
        return self.label
