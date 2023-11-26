# translator/urls.py
from django.urls import path
from .views import translate

urlpatterns = [
    path('', translate, name='translate'),
]
