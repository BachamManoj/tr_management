from django.db import models

# Create your models here.
class Register(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    class Meta:
        db_table="Register"