from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages

# Create your views here.

""" 
Login system from: https://www.geeksforgeeks.org/user-authentication-system-using-django/
"""

def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not User.objects.filter(username=username).exists():
            messages.error(request,'Invalid Username')
            return redirect('/login/')

        student = authenticate(username=username,password=password)
    
        if student is None:

            messages.error(request,'Invalid Username')
            return redirect('/login/')
        else:

            login(request,student)
            return redirect('/home/')
    
    return render(request,'login.html')

def registrationPage(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        student = User.objects.filter(username=username)

        if student.exists():
            messages.error(request, "Username already taken!")
            return redirect("/registration/")
        
        student = User.objects.create_user(
            username=username
        )

        student.set_password(password)
        student.save()

        messages.info(request,"Welcome future olympian!")
        return redirect('/home/')
    
    return render(request,'register.html')

def home(request): # for looking at progress
    return render(request, 'home.html')

def calendar(request):
    return render(request,'calendar.html')

def settings(request):
    return render(request, 'settings.html')

def groups(request):
    return render(request,'groups.html')

def leaderboard(request):
    return render(request,'leaderboard.html')

def training_options(request):
    return render(request, 'training_options.html')