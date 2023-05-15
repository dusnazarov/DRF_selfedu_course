

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('myapp.urls')),
    
    path('drf-auth/', include('rest_framework.urls')),
    path('drf-auth/login/', include('rest_framework.urls')),
    path('drf-auth/logout/', include('rest_framework.urls')),
    
    
]