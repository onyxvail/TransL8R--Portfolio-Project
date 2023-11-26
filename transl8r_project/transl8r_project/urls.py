from django.contrib import admin
from django.urls import include, path
from translator.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('translator/', include('translator.urls')),
    path('', home, name='home'),
]
