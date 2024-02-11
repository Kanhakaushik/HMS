from django.db import models

class DataSignup(models.Model):
    name=models.CharField(max_length=200)
    email=models.EmailField()
    password=models.CharField(max_length=200)
    cpassword=models.CharField(max_length=200)
    
    
