from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
from core.models import  BaseModel
from core.views import _genref

MINIATURE = ""

class Profile(BaseModel):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    code_bank = models.CharField(max_length=50)
    miniature=models.TextField(default=MINIATURE)

    def __str__(self):

        return self.reference

    def getfull_name(self):

        return f'{self.fname} {self.lname}'

    def generate(self):
        while True:
            random = _genref(35)
            if Profile.objects.filter(reference=random).exists():
                continue
            self.reference=random
            break
        return self.reference

    def save(self, *args, **kwargs):
        if self.pk is None :
            self.generate()
        super(Profile, self).save(*args, **kwargs) # Call the real save() method

class User(BaseModel , AbstractUser):
    user_permission=models.ForeignKey("core.AppPermission",on_delete=models.CASCADE)
    prof=models.ForeignKey("users.Profile",on_delete=models.CASCADE)

    def __str__(self):

        return self.reference

    def generate(self):
        while True:
            random = _genref(35)
            if User.objects.filter(reference=random).exists():
                continue
            self.reference=random
            break
        return self.reference

    def save(self, *args, **kwargs):
        if self.pk is None :
            self.generate()
        super(User, self).save(*args, **kwargs) # Call the real save() method

class Prime(BaseModel):
    target = models.ForeignKey("users.User",on_delete=models.CASCADE)
    amount = models.FloatField()
    code_bank = models.CharField(max_length=50)


    def __str__(self):

        return self.reference

    def generate(self):
        while True:
            random = _genref(35)
            if Prime.objects.filter(reference=random).exists():
                continue
            self.reference=random
            break
        return self.reference

    def save(self, *args, **kwargs):
        if self.pk is None :
            self.generate()
        super(Prime, self).save(*args, **kwargs) # Call the real save() method

class Renion(BaseModel):
    target = models.ForeignKey("users.User",on_delete=models.CASCADE)
    date_renion = models.DateTimeField()

    def __str__(self):

        return self.reference

    def generate(self):
        while True:
            random = _genref(35)
            if Renion.objects.filter(reference=random).exists():
                continue
            self.reference=random
            break
        return self.reference

    def save(self, *args, **kwargs):
        if self.pk is None :
            self.generate()
        super(Renion, self).save(*args, **kwargs) # Call the real save() method

class Signale(BaseModel):
    target = models.ForeignKey("users.User",on_delete=models.CASCADE)
    description = models.TextField()
    status = models.ForeignKey("users.SignaleStatus",on_delete=models.CASCADE)     

    def __str__(self):

        return self.reference

    def generate(self):
        while True:
            random = _genref(35)
            if Signale.objects.filter(reference=random).exists():
                continue
            self.reference=random
            break
        return self.reference

    def save(self, *args, **kwargs):
        if self.pk is None :
            self.generate()
        super(Signale, self).save(*args, **kwargs) # Call the real save() method

class SignaleStatus(models.Model):
    label = models.CharField(max_length=50)

    def __str__(self):
        return sefl.label    