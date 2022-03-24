from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('index/',views.index,name='index'),
    path('home/',views.home,name='home'),
    path('signup/',views.signup,name='signup'),
    path('signin/',views.signin,name='signin'),
    path('loginpage/',views.loginpage,name='loginpage'),
    path('viewUsers/',views.viewUsers,name='viewUsers'),
    path('updateuser/<int:id>',views.updateuser,name='updateuser'),
    path('deleteuser/<int:id>',views.deleteUser,name='deleteUser'),
]
