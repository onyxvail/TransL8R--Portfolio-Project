# translator/models.py

from django.db import models

class Translation(models.Model):
    original_text = models.TextField()
    translated_text = models.TextField()
