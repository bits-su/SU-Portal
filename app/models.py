from django.db import models
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

# TODO: Add functionality to display post of SU members.
#       Probably another model('postholders') with OneToOne connection to User 
