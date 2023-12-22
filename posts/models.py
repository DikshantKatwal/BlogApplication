from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    Author_name = models.CharField(max_length=70)
    title = models.CharField(max_length=70)
    desc = models.CharField(max_length=500)
    upload_date = models.DateTimeField(default= datetime.now, blank = True)

