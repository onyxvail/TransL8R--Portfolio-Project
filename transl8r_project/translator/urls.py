# translator/urls.py
from django.urls import path
from .views import translate
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('translate/', translate, name='translate'),
]

# transl8r_project/urls.py
urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('translator.urls')),  # Include translator app URLs
]
