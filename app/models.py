from django.db import models

# Create your models here.


class Contact(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=255)
    username = models.CharField(max_length=255, unique=True)
