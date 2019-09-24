from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.shortcuts import redirect
# Create your views here.


def home(request):
    return render(request,'Main/index.html')


def login_request(request):
    form = AuthenticationForm()
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            print("dkhal")
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username = username, password=password)
            if user is not None:
                login(request,user)
                messages.success(request, "Logged in successfully")
                return redirect('home')
            else:
                messages.info(request,"User dosn't exist")
        else:
            messages.info(request,"Invalid Syntaxe")
    redirect('home')
    return render(request,"Main/login.html", {"form":form})

def logout_request(request):
    logout(request)
    return redirect('home')

# def homeLogged(request):
#     return render(request,'Main/')