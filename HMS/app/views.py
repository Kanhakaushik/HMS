from django.shortcuts import render
from .models import *
# from django.shortcuts import render

def home(request):
    return render(request,'app/index.html')

def about(request):
    return render(request,'app/about.html')

def contact(request):
    return render(request,'app/contact.html')

def room(request):
    return render(request,'app/room.html')

def gallery(request):
    return render(request,'app/gallery.html')


# ----------------------------------

def login(request):
    return render(request,'app/login.html')

def register(request):
    if request.POST:
        name=request.POST['name']
        email=request.POST['email']
        password=request.POST['password']
        cpassword=request.POST['cpassword']
        user=request.POST['user']

        if user=='admin':
            valid=Admin_registration.objects.filter(Email=email)
            if valid:
                msg="User alredy exist"
                return render(request,'app/register.html',{'msg':msg})
            if password==cpassword:
                Admin_registration.objects.create(
                    Name=name,
                    Email=email,
                    Password=password,
                    Cnf_password=cpassword
                )
                msg="Registrerion successfully"
                return render(request,'app/login.html',{'msg':msg})
            else:
                msg="Password and Confirm password are not match"
                return render(request,'app/register.html',{'msg':msg})

        else:
            valid=Manager_registration.objects.filter(Email=email)
            if valid:
                msg="User alredy exist"
                return render(request,'app/register.html',{'msg':msg})
            
            if password==cpassword:
                Manager_registration.objects.create(
                    Name=name,
                    Email=email,
                    Password=password,
                    Cnf_password=cpassword
                )
                msg="Registrerion successfully"
                return render(request,'app/login.html',{'msg':msg})
            else:
                msg="Password and Confirm password are not match"
                return render(request,'app/register.html',{'msg':msg})
               
    else:
        msg="change method again post"
        return render(request,'app/register.html')

def login_Data(request):
    name=request.POST['name']
    email=request.POST['email']
    password=request.POST['password']
    user=request.POST['user']

    if user=='admin':
        data=Admin_registration.objects.get(Email=email)
        if password==data.Password:

            Name=data.Name
            Email=data.Email

            request.session['Name']=Name
            request.session['Email']=Email

            admin_detail={
                'Name':Name ,
               'Email':Email }
        return render(request,"app/dashboard.html",{'data':admin_detail})

def logout(request):
    if "Name" in request.session:
        # del request.session["Name"]
        request.session.flush()
    return render(request,'app/index.html')
