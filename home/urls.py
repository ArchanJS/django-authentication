from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("",views.index,name="index"),
    path("login",views.loginPage,name="login"),
    path("logout",views.logoutPage,name="logout")
]