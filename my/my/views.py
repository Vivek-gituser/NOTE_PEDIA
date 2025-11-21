from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from  django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


def login(reqrest):
    if reqrest.method=='POST':  
        mail=request.POST.get('email')
        passw=request.POST.get('password')
        val=authenticate(request,username=mail,password=passw)
        if val is not None:
            login(request,mail)
            redirect(reqrest,'dashbord.html')
    
    return render(request,'index.html')
def signup(request):
    usernm=request.POST.get('username')
    passw=request.POST.get('password')
    email=request.POST.get('email')
    user=User.object.create_user(username=usernm,password=passw,email=email)
    login(request,user)

