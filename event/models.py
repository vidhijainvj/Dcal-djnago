from django.db import models
import datetime


# Create your models here.

class event(models.Model):
    title = models.CharField(max_length=122)
    date = models.CharField(max_length=50, default='Thu Nov 03 2022')
    start_time = models.TimeField(auto_now_add=False)
    end_time = models.TimeField(auto_now_add=False)
    imp = models.CharField(max_length=30, default='notimp')


    def __str__(self):
        return self.title