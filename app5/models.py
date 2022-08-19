from django.db import models

# Create your models here.

class UserData(models.Model): # class Model is called from models (check package)
    username = models.CharField(max_length= 100)
    phone_no = models.BigIntegerField()
    dob = models.DateField()
    email = models.CharField(max_length= 100)
    pswd = models.CharField(max_length= 100)

