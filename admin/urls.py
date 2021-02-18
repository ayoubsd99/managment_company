from  django.urls import  path

from .views import dashboad,users,primes,groups,meetings

urlpatterns = [
    path('Dashboard/',dashboad.DashboardView.as_view(),name='dashboard'),
    path('users/',users.UsersView.as_view(),name='users'),
    path('user/<str:user_reference>/',users.UserView.as_view(),name='user'),
    path('deleteuser/<str:user_reference>/',users.DeleteUser,name='deleteuser'),
    path('createuser/',users.CreateUser,name='createuser'),

]
