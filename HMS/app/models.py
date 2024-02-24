from django.db import models

class Admin_registration(models.Model):
    Name=models.CharField(max_length=200)
    Email=models.EmailField()
    Password=models.CharField(max_length=200)
    Cnf_password=models.CharField(max_length=200)


class Manager_registration(models.Model):
    Name=models.CharField(max_length=200)
    Email=models.EmailField()
    Password=models.CharField(max_length=200)
    Cnf_password=models.CharField(max_length=200)
    
    
class Rooms(models.Model):
    Room_type=models.CharField(max_length=20)
    Room_Number=models.CharField(max_length=5)

    def __str__(self):
        return self.Room_Number

class Room_book(models.Model):
    Name=models.CharField(max_length=200)
    Email=models.EmailField()
    Members=models.CharField(max_length=10)
    room_allotted=models.ManyToManyField(Rooms)

    def __str__(self):
        return self.Name

