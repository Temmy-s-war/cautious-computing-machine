from django.shortcuts import render, redirect
from django.http import HttpResponse
from authentication.models import RegInsert
from django.contrib import messages
from authentication.models import RegInsert
from django.contrib.auth import authenticate, login
#from django.contrib.auth.model import user


# Create your views here.
def home(request):
    return render(request, "archive/home.html")

def landing(request):
    return render(request, "archive/landing.html")

def index(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password = password)

        if user is not None:
            login(request, saverecord)
            fname = user.fname
            return render(request, "archive/landing.html", {'fname':fname})

        else: messages.error (request, "invalid credentials")
        return redirect('home')

    return render(request, "archive/index.html")

def signup(request):
    if request.method == 'POST':
        print('successful')
        if request.POST.get('username') and request.POST.get('fname') and request.POST.get('lname') and request.POST.get('email') and request.POST.get('Password') and request.POST.get('PasswordConfirmation'):
            saverecord = RegInsert()
            saverecord.username=request.POST.get('username')
            saverecord.fname=request.POST.get('fname')
            saverecord.lname=request.POST.get('lname')
            saverecord.email=request.POST.get('email')
            saverecord.Password=request.POST.get('Password')
            saverecord.PasswordConfirmation=request.POST.get('PasswordConfirmation')

            saverecord.save()
            messages.success(request, 'Record saved successfully')
         , "archive/home.html")
    return render(request, "archive/signup.html")
