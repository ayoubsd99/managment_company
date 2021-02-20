from  django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from django.views import  View

from users.models import User,Renion,RenionStatus
from core.models import AppPermission

APPLICATION = "administration/meetings"

class MeetingsView(View):
    view_name = 'meetings'
    template = f'{APPLICATION}/{view_name}.html'
    def get(self,request,*args,**kwargs):
        context = {
            'meetings':Renion.objects.all()
        }
        return render(request,self.template,context)

class CreateMeeting(View):
    view_name = 'createmeeting'
    template = f'{APPLICATION}/{view_name}.html'
    def get(self,request,*args,**kwargs):
        s=get_object_or_404(AppPermission,label='seller')
        m=get_object_or_404(AppPermission,label='manager')
        context = {
            'sellers':User.objects.filter(deleted=False,user_permission=s),
            'managers':User.objects.filter(deleted=False,user_permission=m),
            'status':RenionStatus.objects.all()

        }
        return render(request,self.template,context)

    def post(self,request,*arg,**kwargs):
        target = request.POST.get('target')
        date_meeting = request.POST.get('date_meeting')
        meeting_statu = request.POST.get('status')
        print(request.POST)
        if target == "" or date_meeting == "" or meeting_statu == "":
            messages.warning(request,'all fields are required')
            return redirect('createmeeting')
        user = get_object_or_404(User,reference=target)
        st = get_object_or_404(RenionStatus,label=meeting_statu)
        metting = Renion.objects.create(target=user,date_renion=date_meeting,status=st)  
        messages.success(request,'meeting added successfully,Happy meeting')  
        return redirect('meetings')

