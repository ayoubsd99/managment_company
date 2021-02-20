from django.shortcuts import render,get_object_or_404,redirect
from django.views import  View
from django.contrib import  messages

from core.models import AppPermission
from chat.models import  ChatRoom
from users.models import  User
APPLICATION = "administration/rooms"

class RoomsView(View):
    view_name = 'rooms'
    template = f'{APPLICATION}/{view_name}.html'
    def get(self,request,*args,**kwargs):
        context = {
            'rooms':ChatRoom.objects.all()
        }
        return render(request,self.template,context)

class RoomView(View):
    view_name = 'room'
    template = f'{APPLICATION}/{view_name}.html'
    def get(self,request,*args,**kwargs):
        room_ref = kwargs.get('room_reference')
        chat = ChatRoom.objects.get(reference=room_ref)
        perad = AppPermission.objects.get(label='admin')
        context = {
            'admin':User.objects.get(is_superuser=True,user_permission=perad),
            'users':User.objects.filter(is_superuser=False,chat_room=chat)
        }
        return render(request,self.template,context)

class DeleteRoom(View):
    def get(self,request,*args,**kwargs):
        room_ref = kwargs.get('room_reference')
        room = get_object_or_404(ChatRoom,reference=room_ref)
        room.deleted = not room.deleted
        room.save()
        messages.success(request,'Chat rooms desactivated succssessfuly')
        return redirect('rooms')

