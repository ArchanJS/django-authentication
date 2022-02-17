from django.shortcuts import redirect, render,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate

# Create your views here.

# username random randomguy@123

def index(request):
    if request.user.is_anonymous:
        return redirect('/login')
    return render(request,"index.html")
def loginPage(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username,password=password)
        login(request,user)
        if user is not None:
            return redirect("/")
        else:
            return render(request,"login.html")
    if request.user.is_anonymous:
        return render(request,"login.html")
    else:
        return render(request,"index.html")
def logoutPage(request):
    logout(request)
    return redirect("/login")