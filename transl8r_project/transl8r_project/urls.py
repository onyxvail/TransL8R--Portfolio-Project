# transl8r_project/urls.py
from django.contrib import admin
from django.urls import path, include
from translator.views import signup, login
from django.shortcuts import redirect


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('translator/', include('translator.urls')),
    path('signup/', signup, name='signup'),
    path('login/', login, name='login'),
    path('', lambda request: redirect('translator/', permanent=False)),
]
