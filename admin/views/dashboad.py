from django.shortcuts import  render,redirect


from django.views import View
from users.models import User,Renion,Prime,Signale
APPLICATION = "administration"

class DashboardView(View):
    view_name = 'dashboard'
    template = f'{APPLICATION}/{view_name}.html'
    def get(self,request,*args,**kwargs):
        if request.user.is_authenticated:

            context = {
                'signales':Signale.objects.filter(status="pending"),
                'renions':Signale.objects.filter(status='Pending')
            }
            return render(request,self.template,context)    

        return redirect('login')
