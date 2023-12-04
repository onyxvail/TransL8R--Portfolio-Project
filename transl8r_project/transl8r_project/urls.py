from django.contrib import admin
from django.urls import path , include
from translator import views

# from translator.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('translator/', include('translator.urls')),
    #path('', home, name='home'),
    path('', include('translator.urls')),
    path('', views.home, name='home'),
]
