from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
from .models import User
# Create your views here.

def index(request):
    return render(request,'login.html')

def home(request):
    return render(request,'home.html')


def signup(request):
    return render(request,'signup.html')

def signin(request):
    if request.method =='POST':
        u_name=request.POST['u_name']
        password=request.POST['password']
        full_name=request.POST['full_name']
        address=request.POST['address']
        age=request.POST['age']
        userdata=User(u_name=u_name,password=password,full_name=full_name,address=address,age=age)
        userdata.save()

        return render(request,'signin.html')
    else:
        return render(request,'signin.html')