from django.shortcuts import  render,redirect,get_object_or_404
from django.views import View
from django.contrib import  messages

import cloudinary.uploader

from users.models import User,Profile
from chat.models import ChatRoom
from core.views import check_email,check_phone
from core.models import AppPermission

APPLICATION = 'administration'

class UsersView(View):
    def get(self,request,*args,**kwargs):
        view_name = 'users'
        template = f'{APPLICATION}/{view_name}.html'
        context = {
            "users":User.objects.filter(user_permission__in=['manager','seller'])
        }
        return render(request,self.template,context)

class UserView(View):
    def get(self,request,*args,**kwargs):
        view_name = 'user'
        template = f'{APPLICATION}/{view_name}.html'
        user_ref = kwargs.get('user_reference')
        context = {
            "users":get_object_or_404(User,reference=user_ref)
        }
        return render(request,self.template,context)

def DeleteUser(request):
    user_ref = request.GET.get('user_reference')
    user = get_object_or_404(User,reference=user_ref)

    user.deleted = not deleted
    messages.success(request,'user desactivted successfuly')
    return redirect('users') 

class CreateUser(View):
    view_name = 'createuser'
    template = f'{APPLICATION}/{view_name}.html'
    def get(self,request,*args,**kawargs):
        context = {
            'managesrs':User.objects.filter(user_permission="manager").filter(dalated=False),
            'permissions': AppPermission.objects.filter(label__in=['manager','seller'])
        }
        return render(request,self.template,context)
    def post(self,request,*args,**kwargs):

        fname = request.POST.get('fname')
        lname = request.POST.get('lname')    
        email = request.POST.get('email')    
        phone = request.POST.get('phone')    
        miniature = request.FILES["miniature"]
        username = request.POST.get('username')    
        password = request.POST.get('password')    
        code_bank = request.POST.get('code_bank')    
        permission = request.POST.get('permission')
        manager = request.POST.get('manager')

        if(fname =='' or lname =='' or email =='' or phone =='' or username =='' or password =='' or code_bank =='' or permission == ''):
            messages.warning(request,'all fields are required')

        elif not check_email(email):
            messages.warning(request,'email user not valide try add an other one')
        elif not check_phone(phone):
            messages.warning(request,'phone number not valid try add an other one')
        elif permission == 'manager':
            name = f'Mr-{lname}-room' 
            try:
                response = cloudinary.uploader.upload(miniature)
                url = response['secure_url']
                chat_room = ChatRoom(room_name=name)
                prof = Profile(lname=lname,fname=fname,phone=phone,email=email,miniature=url)
                permi = get_object_or_404(AppPermission,label=permission)
                user = User(prof=prof,user_permission=permi,chat_room=chat_room)
                chat_room.save()
                prof.save()
                user.save()
                messages.success(request,'manager added successfuly')
                return redirect('users')
            except:
                messages.error(requset,'faield to add manager ')
                return redirect('createuser')
        elif permission == 'seller':
            if(manager == ''):
                messages.warning(request,'please sekect sum manager for that seller')
                return redirect('createuser')
            try:
                response = cloudinary.uploader.upload(miniature)
                url = response['secure_url']
                prof_m = Profile.objects.get(lname=manager)
                manage = get_object_or_404(User,user_permission='manager',prof=prof_m)
                prof = Profile(lname=lname,fname=fname,phone=phone,email=email,miniature=url)
                permi = get_object_or_404(AppPermission,label=permission)
                user = User(prof=prof,user_permission=permi,chat_room=manage.chat_room)
                prof.save()
                user.save()
                messages.success(request,'seller added successfuly')
                return redirect('users')
            except:
                messages.error(requset,'faield to add seller')
                return redirect('createuser')
            else:
                messages.error(request,'failed to add some user error data base')    

class UpdateUser(View):
    view_name = 'updateuser'
    template = f'{APPLICATION}/{view_name}.html'
    def get(self,request,*args,**kwargs):
        user_ref = kwargs.get('user_reference')
        user = get_object_or_404(User,reference=user_ref)
        if user.user_permission.label == 'manager':
            context = {
                'user':get_object_or_404(User,reference=user_ref)
                }
        else:
            context = {
                'user':get_object_or_404(User,reference=user_ref),
                'managers':User.objects.filter(deleted=False,user_permission='manager')
                }                    
        return render(request,self.template,context)

    def post(self,request,*args,**kwargs):

        reference = request.POST.get('reference')
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')    
        email = request.POST.get('email')    
        phone = request.POST.get('phone')    
        miniature = request.FILES["miniature",None]
        username = request.POST.get('username')    
        manager = request.POST.get('manager')

        if(fname =='' or lname =='' or email =='' or phone =='' or username =='' or password =='' or code_bank =='' or permission == ''):
            messages.warning(request,'all fields are required')

        elif not check_email(email):
            messages.warning(request,'email user not valide try add an other one')
        elif not check_phone(phone):
            messages.warning(request,'phone number not valid try add an other one')
        elif permission == 'manager':
            name = f'Mr-{lname}-room' 
            try:
                user = get_object_or_404(User,reference=reference)
                prof =get_object_or_404(Profile,user.prof)
                if miniature is not None:
                    response = cloudinary.uploader.upload(miniature)
                    prof.miniature= response['secure_url']
                prof.fname=fname
                prof.fname=lname    
                prof.fname=email    
                prof.fname=phone    
                prof.fname=username    
                prof.save()
                messages.success(request,'manager updated successfuly')
                return redirect('users')
            except:
                messages.error(requset,'faield to update manager ')
                return redirect('createuser')
        elif permission == 'seller':
            if(manager == ''):
                messages.warning(request,'please sekect sum manager for that seller')
                return redirect('createuser')
            try:
                user = get_object_or_404(User,reference=reference)
                prof =get_object_or_404(Profile,user.prof)
                if miniature is not None:
                    response = cloudinary.uploader.upload(miniature)
                    prof.miniature= response['secure_url']
                manager_prof = get_object_or_404(Profile,email=manager)    
                manag = User.objects.filter(user_permission='manager',prof=manager_prof)
                room =  manag.chat_room    
                prof.fname=fname
                prof.fname=lname    
                prof.fname=email    
                prof.fname=phone    
                prof.fname=username
                user = get_object_or_404(User,prof=prof)
                user.chat_room= room    
                prof.save()
                user.save()
                messages.success(request,'seller updated successfuly')
                return redirect('users')
            except:
                messages.error(requset,'faield to update seller')
                return redirect('createuser')
            else:
                messages.error(request,'failed to update user error data base')    
         