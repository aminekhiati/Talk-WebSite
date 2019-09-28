from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from .forms import *

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
                return redirect('homeLogged')
            else:
                messages.info(request,"User dosn't exist")
        else:
            messages.info(request,"Invalid Syntaxe")
    return render(request,"Main/login.html", {"form":form})

def logout_request(request):
    logout(request)
    return redirect('home')


@login_required
def homeLogged(request):
    return render(request,'Main/home.html')


def signup(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        User.objects.create_user(username=first_name, password=password , last_name=last_name , first_name=first_name , email=email )
        authenticate_user = authenticate(username=first_name,password=password)
        login(request,authenticate_user)
        return redirect('homeLogged')

    return render(request,'Main/signUp.html')