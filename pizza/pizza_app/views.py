
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User

from .models import CustomerModel, PizzaModel

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


def userSignup(request):
    username=request.POST['username']
    password=request.POST['password']
    phoneno=request.POST['phoneno']

    if User.objects.filter(username=username).exists():
        messages.add_message(request,messages.ERROR,"User already exists")
        return redirect("homepage")

    User.objects.create_user(username=username,password=password).save()
    lastObject=len(User.objects.all())-1
    CustomerModel(id=User.objects.all()[int(lastObject)].id ,phoneno=phoneno).save()
    messages.add_message(request,messages.ERROR,"User successfully created")
    return redirect('homepage')


def loginpageView(request):

    return render(request,'pizza-app/login.html')

def userLogin(request):
    username=request.POST['username']
    password=request.POST['password']

    user = authenticate( username=username,password=password)
    print(user)


    if user is not None:
        login(request,user)
        return redirect("customerpage")

    if user is None:

        messages.add_message(request,messages.ERROR,"invalid username or password")
        
        return redirect('loginpageView')

def customerPageView(request):
    return render(request,"pizza-app/customerpage.html")