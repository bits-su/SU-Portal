from django.db import models
from django import forms
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator


class User(AbstractUser):
    image = models.ImageField(blank=True)
    phone = models.CharField(
        max_length = 10,
        validators=[
            RegexValidator(
                regex='^[0-9]{10}$',
                message='Only 10 digit integer allowed',),]
            )

class Complaint(models.Model):
    complaint_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50,unique=False)
    complaint = models.TextField(max_length=3000,unique=False)
    uploadedby = models.ForeignKey(User,verbose_name="complaint-logger",on_delete=models.CASCADE)

# TODO: Add functionality to display post of SU members.
#       Probably another model('postholders') with OneToOne connection to User
