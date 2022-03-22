from django.db import models


class User(models.Model):
    u_name=models.CharField(max_length=20)
    password=models.CharField(max_length=20)
    full_name=models.CharField(max_length=40)
    address=models.TextField()
    age=models.IntegerField()
                         