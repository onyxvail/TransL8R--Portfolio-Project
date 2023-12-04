# translator/models.py
from django.db import models

class Contact(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField()
    country = models.CharField(max_length=100)
    subject = models.TextField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
