from django.db import models

# Create your models here.

class Detect(models.Model):
    cname = models.CharField(max_length=20, blank=True, null=True)
    ctime = models.DateTimeField(blank=True, null=True)
    cpercent = models.IntegerField(blank=True, null=True)
    cid = models.CharField(max_length=20, blank=True, null=True)
