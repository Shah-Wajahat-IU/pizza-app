from django.contrib import admin
from django.contrib.auth import admin
from django.urls import path
from . views import addpizza, adminLoging, authenticateadmin,adminHomeView,adminLogoutView, customerPageView, homePage, loginpageView, pizzaDelete, userLogin, userSignup

urlpatterns = [
    
    path("admin/",adminLoging,name="adminlogin"),
    path("adminauthenticate/",authenticateadmin),
    path('admin/homepage/',adminHomeView, name="adminhomepage"),
    path('logoutadmin/',adminLogoutView),
    path("addpizza/",addpizza),
    path("pizzadelete/<int:pizzapk>/",pizzaDelete),
    path("",homePage,name="homepage"),
    path('signup/',userSignup),
    path('customer/loginpage/',loginpageView,name="loginpageView"),
    path("customer/login/",userLogin,name="customerlogin"),
    path('customer/page',customerPageView,name='customerpage')
]
