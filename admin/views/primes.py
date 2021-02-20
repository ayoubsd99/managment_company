from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import  messages
from django.views import View

from users.models import Prime,User
from core.models import AppPermission

APPLICATION = "administration/primes"

class PrimsView(View):
    view_name = 'primes'
    template = f'{APPLICATION}/{view_name}.html'
    def get(self,request,*args,**kwargs):
        context = {
            'primes':Prime.objects.all()
        }
        return render(request,self.template,context)

class CreatePrime(View):
    view_name = 'createprime'
    template = f'{APPLICATION}/{view_name}.html'
    def get(self,request,*args,**kwargs):
        s=get_object_or_404(AppPermission,label='seller')
        m=get_object_or_404(AppPermission,label='manager')
        context = {
            'sellers':User.objects.filter(deleted=False,user_permission=s),
            'managers':User.objects.filter(deleted=False,user_permission=m),
        }
        return render(request,self.template,context)

    def post(self,request,*args,**kwargs):
        target = request.POST.get('target')
        amount = request.POST.get('amount')
        code_bank = request.POST.get('code_bank')
        if target =="" or amount == "" or code_bank == "":
            messages.warning(request,'all fields are required')
            return redirect('createprime') 
        user = get_object_or_404(User,reference=target)         
        try:
            print(user)
            
            Prime.objects.create(target=user,amount=amount,code_bank=code_bank)
            print('gggggggggg')
        except:
            print('hhhhhhhh')
            messages.error(request,'failed to add prime to that user ,error base doner')
        return redirect('primes')




