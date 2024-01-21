from django.db import models

from django.contrib.auth.models import User

class event(models.Model):

    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, null=True, blank=True)
    banner = models.ImageField(upload_to='', null=True, blank=True)
    email = models.EmailField(max_length=124, null=True, blank=True)
    phone = models.CharField(max_length=15, null=True, blank=True)
    adress = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=30, null=True, blank=True)
    state = models.CharField(max_length=30, null=True, blank=True)
    country = models.CharField(max_length=30, null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    start_time = models.TimeField(null=True, blank=True)
    end_time = models.TimeField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'{str(self.id)} - {str(self.name)}'
    
class participant(models.Model):
    events = models.ForeignKey(event, on_delete=models.CASCADE, default=1)
    name = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(max_length=124, null=True, blank=True)

    def __str__(self):
        return f'{str(self.events)} - {str(self.name)}'
