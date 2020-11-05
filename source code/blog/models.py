from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
        
class Crop(models.Model):
    cropname = models.CharField(max_length=100)
    discription = models.TextField()  
    crop_season = models.CharField(max_length=100)
    crop_climate = models.CharField(max_length=100)

    def __str__(self):
        return self.cropname

#    def get_absolute_url(self):
#        return reverse('crop-detail', kwargs={'pk': self.pk})
