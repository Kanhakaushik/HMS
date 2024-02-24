from django.shortcuts import render
from .models import *
from .forms import *
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

def main(request):
    return render(request,'app/admindash.html')



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

def room_book(request):
    Roomfrom=RoomsFrom()
    RoombookFrom=Room_bookFrom()
    return render(request,'app/room_book.html',{'Roomfrom':Roomfrom,'RoombookFrom':RoombookFrom})

def add_room(request):
    Roomtype=request.POST['Room_type']
    RoomNumber=request.POST['Room_Number']

    Rooms.objects.create(
        Room_type=Roomtype,
        Room_Number=RoomNumber,
    )
    Roomfrom=RoomsFrom()
    RoombookFrom=Room_bookFrom()
    return render(request,'app/room_book.html',{'Roomfrom':Roomfrom,'RoombookFrom':RoombookFrom})



def room_allotted(request):
    name=request.POST['Name']
    email=request.POST['Email']
    members=request.POST['Members']
    allotted=request.POST['room_allotted']

    data=Rooms.objects.get(id=allotted)

    Room_book.objects.create(
        Name=name,
        Email=email,
        Members=members,
        room_allotted=data,
    )
   
    Roomfrom=RoomsFrom()
    RoombookFrom=Room_bookFrom()
    return render(request,'app/room_book.html',{'Roomfrom':Roomfrom,'RoombookFrom':RoombookFrom})

def adminlogin(request):
    if request.method=="POST":
        ad_id=request.POST['adminID']
        ad_pass=request.POST['adminPassword']
        admin_data={
            'id': 'admin@hotel.co.in',
            'password':'admin@main'
        }
        user="Admin"
        if(admin_data['id']== ad_id and admin_data['password']== ad_pass):
            return render(request,'app/admindash.html',{'user':user})
    else:
        msg="your password and not match"
        return render(request,'app/login.html',{'msg':msg})
    