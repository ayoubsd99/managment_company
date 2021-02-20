from django.shortcuts import  render,get_object_or_404,redirect
from django.contrib.auth.models import Permission, User
from django.contrib.auth import login,logout,authenticate
from django.views import View
from django.contrib import messages
from users.models import  User

APPLICATION = 'authentification/admin'
class SignInView(View):
    view_name = 'signin'
    template = f'{APPLICATION}/{view_name}.html'
    def get(self,request,*args,**kwargs):

        return render(request,self.template)

    def post(self,request,*arg,**kwargs):

        username = request.POST.get('username')
        password = request.POST.get('password')
        us = User.objects.get(is_superuser=True,username=username,password=password)
        #user = authenticate(username=us.username,password=us.password)
        print(us)
        if us is not None:
            login(request,us)
            return redirect('dashboard')
        messages.error(request,"sorry bu thi admin note exists")
        return redirect('signin')


def lougoutView(request):
    logout(request)
    return redirect("signin")
