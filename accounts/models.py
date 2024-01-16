from django.db import models
from django.contrib.auth.models import User

class UserAccount(models.Model):
    ROLE_CHOICES = [
        ('Patient', 'Patient'),
        ('Doctor', 'Doctor'),
    ]

    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]

    user = models.OneToOneField(User,related_name='account', on_delete=models.CASCADE)
    nid = models.CharField(max_length=20, unique=True, verbose_name="National ID")
    birth_date = models.DateField(null=True, blank=True)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='Patient')
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, blank=True, null=True)
    street_address = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    postal_code = models.CharField(max_length=20, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    

    def __str__(self):
        return f"{self.user.username} - {self.nid} - {self.role}"
