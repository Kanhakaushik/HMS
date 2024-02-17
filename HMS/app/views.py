from django.shortcuts import render
from .models import *

def home(request):
    return render(request,'app/index.html')

def about(request):
    return render(request,'app/about.html')

def contact(request):
    return render(request,'app/contact.html')

def room(request):
    return render(request,'app/room.html')

def service(request):
    return render(request,'app/service.html')

def team(request):
    return render(request,'app/team.html')

def testimonial(request):
    return render(request,'app/testimonial.html')

def bash(request):
    return render(request,'app/bash.html')

def booking(request):
    return render(request,'app/booking.html')

def register(request):
    if request.POST:
        name=request.POST['name']
        email=request.POST['email']
        password=request.POST['password']
        cpassword=request.POST['cpassword']
        user=DataSignup.objects.filter(email=email)

        if user:
            msg="user alredy exist"
            return render(request,'app/register.html')
        else:
            DataSignup.objects.create(
                name=name,
                email=email,
                password=password,
                cpassword=cpassword
            )
            msg="Registrerion successfully"
            return render(request,'app/login.html')
    else:
        msg="change method again post"
        return render(request,'app/register.html')

def login(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']

        # Checking the emailid with database
        user = DataSignup.objects.filter(email=email)
        if user:
            data = DataSignup.objects.get(email=email)
            if data.password == password:
                name = data.name
                email = data.email
                cpassword=cpassword
                user={
                    'name':name,
                   'email':email,
                   'cpassword':cpassword,
                  }
                return render(request,"app/index.html",{'key':user})
            else:
                message = "Password does not match"
                return render(request,"app/login.html",{'msg':message})
        else:
            message = "User does not exist"
            return render(request,"app/register.html",{'msg':message})
 