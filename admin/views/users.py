from django.shortcuts import  render,redirect,get_object_or_404
from django.views import View
from django.contrib import  messages

from time import sleep
from asgiref.sync import sync_to_async
import asyncio
import cloudinary.uploader
from django.utils.decorators import classonlymethod

from users.models import User,Profile
from chat.models import ChatRoom
from core.views import check_email,check_phone
from core.models import AppPermission,City,Country

APPLICATION = 'administration/users'

class UsersView(View):
    view_name = 'users'
    template = f'{APPLICATION}/{view_name}.html'
    def get(self,request,*args,**kwargs):
        context = {
            "users":User.objects.all()
        }
        return render(request,self.template,context)

class UserView(View):
    view_name = 'user'
    template = f'{APPLICATION}/{view_name}.html'
    def get(self,request,*args,**kwargs):
       
        user_ref = kwargs.get('user_reference')
        context = {
            "user":get_object_or_404(User,reference=user_ref)
        }
        return render(request,self.template,context)

class DeleteUser(View):
    def get(self,request,*args,**kwargs):
            
        user_ref = kwargs.get('user_reference')
        user = get_object_or_404(User,reference=user_ref)
        user.deleted = not user.deleted
        user.save()
        messages.success(request,'user desactivted successfuly')
        return redirect('users') 

class CreateUserView(View):

    view_name = 'createuser'
    template = f'{APPLICATION}/{view_name}.html'
    def get(self,request,*args,**kawargs):
        context = {
            'managers':User.objects.filter(deleted=False),
            'permissions': AppPermission.objects.all(),
            'cities':City.objects.all(),
            'countries':Country.objects.all(),
        }
        return render(request,self.template,context)
    
    def post(self,request,*args,**kwargs):

        fname = request.POST.get('fname')
        lname = request.POST.get('lname')    
        email = request.POST.get('email')    
        phone = request.POST.get('phone')
        country =  request.POST.get('country')
        city =  request.POST.get('city')
        miniature = request.FILES["miniature"]
        username = request.POST.get('username')    
        password = request.POST.get('password')    
        code_bank = request.POST.get('code_bank')    
        permission = request.POST.get('permission')
        manager = request.POST.get('manager')

        if(fname =='' or lname =='' or email =='' or phone =='' or username =='' or password =='' or code_bank =='' or permission == ''):
            messages.warning(request,'all fields are required')
            print('creaty fileds')
            

        elif not check_email(email):
            messages.warning(request,'email user not valide try add an other one')
            print('email fileds')
        #elif not check_phone(phone):
        #    messages.warning(request,'phone number not valid try add an other one')
        #    print('phone fileds')

        elif permission == 'manager':
            name = f'Mr-{lname}-{fname}-room' 
            try:
                response = cloudinary.uploader.upload(miniature)
                url = response['secure_url']
                chat_room =  ChatRoom.objects.create(room_name=name)
                print(chat_room)
                permi =   get_object_or_404(AppPermission,label=permission)
                print(permi)
                city =   get_object_or_404(City,label=city)
                country =   get_object_or_404(Country,label=country)
                sleep(5)
                prof=   Profile.objects.create(fname=fname,city=city,country=country,lname=lname,phone=phone,email=email,code_bank=code_bank,miniature=url)
                sleep(5)
                print("profile")
                user =    User.objects.create(prof=prof,user_permission=permi,chat_room=chat_room,username=username,password=password)
                print(user)
                messages.success(request,'manager added successfuly')
                return redirect('users')
            except:
                messages.error(request,'faield to add manager ')
                print('manager not add')
                return redirect('createuser')
        elif permission == 'seller':
            if(manager == ''):
                messages.warning(request,'please sekect sum manager for that seller')
                print('vide maneger')
                return redirect('createuser')
            try:
                response =  cloudinary.uploader.upload(miniature)
                url = response['secure_url']
                print(manager)
                manage = get_object_or_404(User,reference=manager)
                print(manage)
                permi = get_object_or_404(AppPermission,label=permission)
                print(permi)
                city =   get_object_or_404(City,label=city)
                print(city)
                country =   get_object_or_404(Country,label=country)
                print(country)
                print(manage.chat_room)
                chat_room=get_object_or_404(ChatRoom,reference=manage.chat_room)
                print(chat_room.room_name)
                prof=   Profile.objects.create(fname=fname,city=city,country=country,lname=lname,phone=phone,email=email,code_bank=code_bank,miniature=url)
                print(prof.lname)
                user =   User.objects.create(prof=prof,user_permission=permi,chat_room=chat_room,username=username,password=password)
                messages.success(request,'seller added successfuly')
                return redirect('users')
            except:
                messages.error(request,'faield to add seller')
                print("faield to add seller")
                return redirect('createuser')
            else:
                messages.error(request,'failed to add some user error data base')   
        return redirect('createuser')

class UpdateUserView(View):
    view_name = 'updateuser'
    template = f'{APPLICATION}/{view_name}.html'
    def get(self,request,*args,**kwargs):
        user_ref = kwargs.get('user_reference')
        user = get_object_or_404(User,reference=user_ref)
        if user.deleted == True:
            messages.warning(request,'this user is not active try activated him the apdated')
            return redirect("users")
        context = {
        'user':user,
        'managers':User.objects.filter(deleted=False),
        'permissions':AppPermission.objects.all(),
        'cities':City.objects.all(),
        'countries':Country.objects.all(),
        }                    
        return render(request,self.template,context)

    def post(self,request,*args,**kwargs):
        reference = kwargs.get('user_reference')
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')    
        email = request.POST.get('email')    
        phone = request.POST.get('phone')  
        permission = request.POST.get('permission')  
        code_bank = request.POST.get('code_bank')    
        miniature = request.FILES.get("miniature",False)
        username = request.POST.get('username')    
        manager = request.POST.get('manager',False)
        city = request.POST.get('city')
        country = request.POST.get('country')


        if(fname =='' or lname =='' or email =='' or phone =='' or username ==''  or code_bank =='' or permission == ''):
            messages.warning(request,'all fields are required')

        elif not check_email(email):
            messages.warning(request,'email user not valide try add an other one')
        #elif not check_phone(phone):
        #    messages.warning(request,'phone number not valid try add an other one')
        
        elif permission == 'manager':
            try:
                user = get_object_or_404(User,reference=reference)
                print(user)
                city=get_object_or_404(City,label=city)
                country=get_object_or_404(Country,label=country)
                perm=get_object_or_404(AppPermission,label=permission)
                if miniature is not False:
                    print('img fdalse')
                    response = cloudinary.uploader.upload(miniature)
                    prof = Profile.objects.filter(email=email).update(miniature=response['secure_url'])

                prof = Profile.objects.filter(email=email).update(fname=fname,lname=lname,city=city,country=country,email=email,phone=phone,code_bank=code_bank)
                messages.success(request,'manager updated successfuly')
                return redirect('users')
            except:
                messages.error(request,'faield to update manager ')
                return redirect('users')
        elif permission == 'seller':
            print('hihihi')
            try:
                print('hihihi')
                city=get_object_or_404(City,label=city)
                country=get_object_or_404(Country,label=country)   
                user = get_object_or_404(User,reference=reference)

                if miniature is not False:
                    print('img fdalse')
                    print(user.prof)
                    response = cloudinary.uploader.upload(miniature)
                    prof=Profile.objects.filter(reference=user.prof).update(miniature=response['secure_url'])
                    messages.success(request,'image updated successfuly')
                print('image updated')
                #if manager is not False:
                #    print('room not false')
                #    prof=Profile.objects.filter(reference=user.prof).update(fname=fname,lname=lname,city=city,country=country,email=email,phone=phone,code_bank=code_bank
                #    manage = get_object_or_404(User,reference=manager)
                #    room = get_object_or_404(ChatRoom,reference=manage.chat_room)
                #    user = get_object_or_404(User,reference=reference)
                #    user.objects.filter(reference=user.prof).update(chat_room=room)
                print('room updated')
                prof=Profile.objects.filter(reference=user.prof).update(fname=fname,lname=lname,city=city,country=country,email=email,phone=phone,code_bank=code_bank)
                messages.success(request,'seller updated successfuly')
                return redirect('users')
            except:
                messages.error(request,'faield to update seller')
                return redirect('users')
        else:
                messages.error(request,'failed to update user error data base')    
        return redirect('users') 