from django.db import models

# Create your models here.
class RegInsert(models.Model):
    # id = models.IntegerField( null =False)
    username = models.CharField(max_length=100, null =False)
    fname =  models.CharField(max_length=100, null =False)
    lname =  models.CharField(max_length=100, null =False)
    email =  models.EmailField(primary_key = True, null =False)
    Password=  models.CharField(max_length=100, null =False)
    PasswordConfirmation=  models.CharField(max_length=100, null =False)
    class Meta:
        db_table = "register"
