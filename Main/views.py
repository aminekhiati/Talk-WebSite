from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import *


# Create your views here.


def home(request):
    return render(request,'Main/index.html')


def login_request(request):
    form = AuthenticationForm()
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username = username, password=password)
            if user is not None:
                login(request,user)
                return redirect('home')
            else:
                messages.info(request,"User dosn't exist")
        else:
            messages.info(request,"Invalid Syntaxe")
    return render(request,"Main/login.html", {"form":form})

def logout_request(request):
    logout(request)
    return redirect('')


@login_required
def homeLogged(request):
    return render(request,'Main/home.html')


def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        User.objects.create_user(username=username, password=password , last_name=last_name , first_name=first_name , email=email )
        authenticate_user = authenticate(username=username,password=password)
        login(request,authenticate_user)
        return redirect('home')

    return render(request,'Main/signUp.html')


@login_required
def profile(request,pk):
    skills = Skill.objects.all()
    interests = Interest.objects.all()
    User.objects.get(pk=pk)

    context ={
        "interests":interests,
        "skills":skills
    }
    return render(request,'Main/profile.html',context)    


@login_required
def theme(request):
    return render(request,'Main/add.html')