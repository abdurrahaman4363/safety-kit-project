
from django.db import models
from accounts.models import UserAccount
from django.contrib.auth.models import User


class Campaign(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='vaccine_campaign/images')
    start_date = models.DateField()
    end_date = models.DateField()
    
    def __str__(self):
        return self.name
    

class Vaccine(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField()
    age = models.CharField(max_length=10)
    dose_number = models.IntegerField(null=True,blank=True)
    campaign = models.ManyToManyField(Campaign, related_name='campaign')
    user_account = models.ForeignKey(UserAccount, on_delete=models.CASCADE, related_name='vaccine',null=True,blank=True)

    def __str__(self):
        if self.user_account and self.user_account.role == 'Doctor':
            return f"{self.name} - {self.user_account.user.username}"


class AvailableTime(models.Model):
    date = models.DateField()

    def __str__(self):
        return f"{self.date}"

class DoseBooking(models.Model):
    patient = models.ForeignKey(User, on_delete=models.CASCADE)
    first_dose = models.ForeignKey(AvailableTime, on_delete=models.CASCADE)
    second_dose = models.DateField(null=True, blank=True)
    phone_number = models.CharField(max_length=15, blank=True)

    def __str__(self):
        return f"{self.patient.username} - {self.first_dose}"



STAR_CHOICES = [
    ("1", "⭐"),
    ("2", "⭐⭐"),
    ("3", "⭐⭐⭐"),
    ("4", "⭐⭐⭐⭐"),
    ("5", "⭐⭐⭐⭐⭐"),
]


class Review(models.Model):
    reviwer = models.ForeignKey(User, on_delete=models.CASCADE)
    campaign = models.ForeignKey(
        Campaign, on_delete=models.CASCADE, related_name="reviews"
    )
    comment = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    rating = models.CharField(choices=STAR_CHOICES, max_length=10)

    def __str__(self):
        return f"Reviewer: {self.reviwer.first_name}; Campaign: {self.campaign.name}"

            
            
  