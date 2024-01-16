from django.contrib import admin
from .models import Vaccine,Campaign,AvailableTime,DoseBooking,Review
# Register your models here.
admin.site.register(Vaccine)
admin.site.register(Campaign)
admin.site.register(AvailableTime)
admin.site.register(DoseBooking)
admin.site.register(Review)