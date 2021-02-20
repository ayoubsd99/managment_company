from django.shortcuts import render,get_object_or_404,redirect
from django.views import View
from django.contrib import messages

from users.models import User,Signale,SignaleStatus

APPLICATION =  "administration/signales"

class SignalesView(View):
    View_name = 'signales'
    template = f'{APPLICATION}/{View_name}.html'

    def get(self,request,*args,**kwargs):
        context = {
            'signels':Signale.objects.all()
        }
        return render(request,self.template,context)

class SignaleView(View):
    view_name = 'signale'
    template = f'{APPLICATION}{view_name}.html'
    def get(self,request,*args,**kwargs):
        signele_ref = kwargs.get('signale_reference')
        context = {
            "signale":get_object_or_404(Signale,reference=signale_ref),
            "status":SignaleStatus.objects.all()
        }
        return render(request,sefl.template,context)

    def post(self,request,*args,kwargs):
        signale_ref = kwargs.get('signale_reference')
        signale_status = request.POST.get('signale_status')
        signele = get_object_or_404(Signale,reference=signale_ref)
        signale.status = signale_status
        signele.save()
        messages.success(request,'signale updated successfuly thank you admin')
        return redirect('signales')

