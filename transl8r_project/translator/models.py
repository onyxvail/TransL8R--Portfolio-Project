# translator/models.py
from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Additional fields for user profile

class TranslationHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    source_text = models.TextField()
    target_text = models.TextField()
    # Additional fields for translation history
