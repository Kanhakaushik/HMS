from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

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

def booking(request):
    return render(request,'app/booking.html')