from django.urls import path


from .views import admin

urlpatterns = [
    path("SignIn/",admin.SignInView.as_view(),name='signin'),
    path("Logout/",admin.lougoutView,name='logout')

]