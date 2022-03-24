from django.shortcuts import redirect, render
from django.shortcuts import render
from django.http import HttpResponse
from .models import User

# Create your views here.

def index(request):
    return render(request,'index.html')

def home(request):
    id=request.session['userid']
    userdata=User.objects.get(id=id)
    return render(request,'home.html', {"userdetails": userdata})


def signup(request):
    return render(request,'signup.html')

def signin(request):
    if request.method =='POST':
        u_name=request.POST['u_name']
        email=request.POST['email']
        password=request.POST['password']
        full_name=request.POST['full_name']
        address=request.POST['address']
        place=request.POST['place']
        userdata=User(u_name=u_name,password=password,full_name=full_name,address=address,place=place,email=email)
        userdata.save()

        return render(request,'signin.html')
    else:
        return render(request,'signin.html')      


def loginpage(request):
    if request.method=="POST":
        u_name=request.POST['u_name']
        password=request.POST['password']
        try:
            userdetails=User.objects.get(u_name=u_name,password=password)
            request.session['userid']=userdetails.id
            return redirect('/home')
        except User.DoesNotExist:
            return render(request,"loginpage.html",{'status':'Login Failed'})
    else:
            return render(request,"loginpage.html")


def viewUsers(request):
    userdata=User.objects.all()
    return render(request,'viewUsers.html', {"userdata":userdata})


def updateuser(request, id):
    if request.method=='POST':
        full_name=request.POST['full_name']
        address=request.POST['address']
        age=request.POST['age']
        u_name=request.POST['u_name']
        password=request.POST['password']
        userdetails=User.objects.filter(id=id).update(full_name=full_name,address=address,password=password,age=age,u_name=u_name)
        return redirect('/viewUsers')
    else:

        userdata=User.objects.get(id=id)
        return render(request,'updateuser.html', {"userdetails":userdata})


def deleteUser(request,id):
    User.objects.filter(id=id).delete()
    return redirect('/viewUsers')
