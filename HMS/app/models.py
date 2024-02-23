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
    
    
# class book_registration(models.Model):
#     Check_in_date=models.DateField(auto_now=True)
#     Check_out_date = models.DateTimeField()
#     A