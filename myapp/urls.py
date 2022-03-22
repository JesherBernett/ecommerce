from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('login/',views.index,name='index'),
    path('',views.home,name='home'),
    path('signup/',views.signup,name='signup'),
    path('signin/',views.signin,name='signin')
]
