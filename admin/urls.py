from  django.urls import  path

from .views import dashboad,users,primes,rooms,meetings,signales

urlpatterns = [
    #base urls
    path('',dashboad.DashboardView.as_view(),name='dashboard'),
    
    # users urls

    path('Users/',users.UsersView.as_view(),name='users'),
    path('User/<str:user_reference>/',users.UserView.as_view(),name='user'),
    path('DeleteUser/<str:user_reference>/',users.DeleteUser.as_view(),name='deleteuser'),
    path('CreateUser/',users.CreateUserView.as_view(),name='createuser'),
    path('UpdateUser/<str:user_reference>/',users.UpdateUserView.as_view(),name='updateuser'),

    #meetings urls
    path('Meetings/',meetings.MeetingsView.as_view(),name='meetings'),
    path('CreateMeeting/',meetings.CreateMeeting.as_view(),name='createmeeting'),


    # Signales urls
    path('Signales/',signales.SignalesView.as_view(),name='signales'),
    path('Signale/<str:signale_reference>/',signales.SignaleView.as_view(),name='signale'),

    # Rooms urls
    path('Rooms/',rooms.RoomsView.as_view(),name='rooms'),
    path('Room/<str:room_reference>/',rooms.RoomView.as_view(),name='room'),
    path('DeleteRom/<str:room_reference>/',rooms.DeleteRoom.as_view(),name='deleteroom'),


    # primes urls
    path('Primes/',primes.PrimsView.as_view(),name='primes'),
    path('Prime/',primes.CreatePrime.as_view(),name='createprime'),

]
