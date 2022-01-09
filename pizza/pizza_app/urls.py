from django.contrib import admin
from django.contrib.auth import admin
from django.urls import path
from . views import adminLoging, authenticateadmin,adminHomeView

urlpatterns = [
    
    path("admin/",adminLoging,name="adminlogin"),
    path("adminauthenticate/",authenticateadmin),
    path('admin/homepage/',adminHomeView, name="adminhomepage")
]
