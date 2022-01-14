
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from .models import PizzaModel

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
        
        return redirect('adminhomepage')



def adminHomeView(request):
    pizza= PizzaModel.objects.all()
    context={
        "pizzas":pizza
    }
    return render(request,"pizza-app/adminhomepage.html", context)


def  addpizza(request):
    name=request.POST['pizzaName']
    price=request.POST['price']

    pizza =PizzaModel(name=name,price=price)
    pizza.save()

    return redirect("adminhomepage")

def adminLogoutView(request):
    logout(request)

    return redirect("adminlogin")

def pizzaDelete(request,pizzapk):
    PizzaModel.objects.filter(id=pizzapk).delete()
    return redirect('adminhomepage')


def homePage(request):
    return render(request,"pizza-app/homePage.html")