
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from django.contrib import messages

# Create your views here.
def adminLoging(request):
    return render(request,"pizza-app/adminLogin.html")


def authenticateadmin(request):
    username=request.POST['username']
    password=request.POST['password']

    user = authenticate( username=username,password=password)


    if user is not None and user.username=='admin':
        login(request,user)
        return redirect("adminhomepage")

    if user is None:

        messages.add_message(request,messages.ERROR,"invalid username or password")
        
        return redirect('adminlogin')



def adminHomeView(request):
    return render(request,"pizza-app/adminhomepage.html")