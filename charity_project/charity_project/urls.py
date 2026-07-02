from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # CHANGE THIS LINE BELOW:
    path('admin/', admin.site.urls), 
    path('', include('core.urls')),         
]
