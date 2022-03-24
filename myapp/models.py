from django.db import models


class User(models.Model):
     full_name=models.CharField(max_length=40)
     place=models.CharField(max_length=50,default="place")
     email=models.EmailField(max_length=254, default="abc@gmail.com")
     address=models.TextField()
     u_name=models.CharField(max_length=20)
     password=models.CharField(max_length=20)
    
    
                         