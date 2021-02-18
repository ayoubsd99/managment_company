from django.db import models
# Create your models here.

from core.models import BaseModel
from core.views import _genref


class ChatRoom(BaseModel):
    room_name=models.CharField(max_length=50)


    def __str__(self):

        return self.reference

    def generate(self):
        while True:
            random = _genref(35)
            if ChatRoom.objects.filter(reference=random).exists():
                continue
            self.reference=random
            break
        return self.reference

    def save(self, *args, **kwargs):
        if self.pk is None :
            self.generate()
        super(ChatRoom, self).save(*args, **kwargs) # Call the real save() method

class Message(BaseModel):
    sender = models.ForeignKey("users.User",on_delete=models.CASCADE)
    content = models.TextField()
    is_read = models.BooleanField(default=False)


    def __str__(self):

        return self.reference

    def generate(self):
        while True:
            random = _genref(35)
            if Message.objects.filter(reference=random).exists():
                continue
            self.reference=random
            break
        return self.reference

    def save(self, *args, **kwargs):
        if self.pk is None :
            self.generate()
        super(Message, self).save(*args, **kwargs) # Call the real save() method