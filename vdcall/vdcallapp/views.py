from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def register(request):
    if request.method=='POST':
       uname=request.POST.get('username')
       email=request.POST.get('email')
       pass1=request.POST.get('pass1')
       pass2=request.POST.get('pass2')
       user = User.objects.filter(username=uname)
       if user.exists():
           messages.error(request,"username already taken")
           return redirect('register')
       if pass1!=pass2:
           messages.error(request,"Your password not matched")
       elif uname=='' or email=='' or pass1=='' or pass2=='':
           messages.info(request,"Please enter details")
       else:
           my_user=User.objects.create_user(uname,email,pass1)
           my_user.save()
           user=authenticate(request,username=uname,email=email,password=pass1)
           login(request,user)
           messages.success(request,"Your account has been successfully registered! ")
           return redirect('home')
    return render(request, 'register.html')


def login_view(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass1')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            messages.success(request,"Succesfully Login")
            login(request,user)
            return redirect('home')
        elif username=='' and pass1=='':
            messages.info(request,"Please enter username and password")
        elif username=='':
            messages.info(request,"Please enter username")
        elif pass1=='':
            messages.info(request,"Please enter password")
        else:
            messages.error(request,"Invalid Username and Password")
    return render(request, 'login.html')

@login_required
def home(request):
    return render(request,"home.html")

@login_required
def videocall(request):
    return render(request,"videocall.html")

@login_required
def logout_view(request):
    logout(request)
    return redirect('Login')

@login_required
def join_room(request):
    if request.method == 'POST':
        roomID = request.POST['roomID']
        if roomID=='':
            messages.error(request,'Please enter room id')
            return redirect('join_room')
        else:
            return redirect("/videocall?roomID=" + roomID)
    return render(request, 'join_room.html')