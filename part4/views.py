from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect
import json
from django.core.serializers.json import DjangoJSONEncoder
import re
from .models import Laptop, Desktop, Order, Feedback
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from itertools import chain
from django.contrib.auth.hashers import check_password
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordResetView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages

# Acknowledgement: https://dev.to/earthcomfy/django-reset-password-3k0l?fbclid=IwAR0F9bvwXVo7I8BSh5es8WxSls5pfnjDgguytDulyH8VHYtO6BE3f7aVhxo
class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
    template_name = 'part4/password_reset.html'
    email_template_name = 'part4/password_reset_email.html'
    subject_template_name = 'part4/password_reset_subject'
    success_message = "We've emailed you instructions for setting your password, " \
                      "if an account exists with the email you entered. You should receive them shortly." \
                      " If you don't receive an email, " \
                      "please make sure you've entered the address you registered with, and check your spam folder."
    success_url = reverse_lazy('index')


# Create your views here.
def loginPage(request):

    page = 'login'
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        try:
            user=User.object.get(username=username)
        except:
            pass

        user=authenticate(request,username=username,password=password)
        
        if user is not None:
            login(request,user)
            return redirect('/part4')
        else:
            pass

    context={'page':page}

    return render(request,'part4/login_register.html',context)

def logoutUser(request):
    logout(request)
    return redirect('/part4')


def registerPage(request):
    page='register'
    context={'page':page}

    if request.method == 'POST':
        username=request.POST.get('username')

        password=request.POST.get('password')
        firstname=request.POST.get('firstname')
        lastname=request.POST.get('lastname')
        email=request.POST.get('email')
        if User.objects.filter(email = email).exists():   

            context={'page':page,'email':email}
            print("email taken")
            return render(request,'part4/login_register.html',context)
        
        user = User.objects.create_user(username, email, password)
        user.first_name=firstname
        user.last_name=lastname
        user.save()

        login(request,user)

        return redirect('/part4')

    return render(request,'part4/login_register.html',context)

def profilePage(request):
    if request.method == 'POST':
        if 'profilechange' in request.POST:
            username=request.POST.get('username')
            firstname=request.POST.get('firstname')
            lastname=request.POST.get('lastname')
            email=request.POST.get('email')
            user = request.user
            user.username=username
            user.email=email
            user.first_name=firstname
            user.last_name=lastname
            user.save()
            login(request,user)

        else:
            user=request.user
            oldpass=request.POST.get('oldPass')
            password=request.POST.get('newPass')

            if check_password(oldpass,user.password):
                try:
                    user.set_password(password)
                    user.save()
                    login(request,user)

                except Exception as e:
                    print("ERROR : "+str(e))
            else:
                messages.warning(request, 'Something isn\'t quite right.')
    messages.success(request, 'Profile details updated.')
    return render(request,'part4/profile.html')


def index(request):
    return render(request, "part4/main.html")


def laptop(request):
    listof = Laptop.objects.all()
    laptopsDB = json.loads(json.dumps(list(listof.values()), cls=DjangoJSONEncoder))
    
    return render(request, "part4/laptop.html", {"laptops": laptopsDB})

def laptopConfig(request, pk):
    laptop = Laptop.objects.get(model=pk)
    return render(request, "part4/laptopConfig.html", {"laptop": laptop})

def bag(request):
    bagItemsCookie = request.COOKIES.get("bagItems")
    
    if bagItemsCookie is not None:
        items = json.loads(request.COOKIES.get("bagItems").replace("%22","\"").replace("%2C",",").replace("%20"," "))
        total = 0
        for item in items:
            total += item["price"]
        return render(request,  "part4/bag.html", {"items": items, "total":total})
    else:
        return render(request,  "part4/bag.html", {"items":[]})

@login_required(login_url='login')
def order(request):

    items = json.loads(request.COOKIES.get("bagItems").replace("%22","\"").replace("%2C",",").replace("%20"," "))
    total = 0
    for item in items:
        total += item["price"]
    Order.objects.create(
        user = request.user,
        total = total,
        items = items,
    )
    response = HttpResponseRedirect('/part4/order-message')
    response.delete_cookie('bagItems')
    response.delete_cookie('bagItems')
    return response

def orderHistory(request):
    orders = Order.objects.filter(user= request.user)
    return render(request, "part4/orderHistory.html", {"orders": orders})

def orderDetails(request, pk):
    order = Order.objects.get(id=pk)
    itemsList = order.items

    total = 0
    print(itemsList)
    for item in itemsList:
        total += item["price"]
        
        # total += int(item["price"])
    return render(request, "part4/orderDetails.html", {"order": order, "total": total})

def deleteOrder(request, pk):
    Order.objects.get(id=pk).delete()
    orders = Order.objects.filter(user= request.user)
    messages.success(request, 'Order deleted')
    return render(request, "part4/orderHistory.html", {"orders": orders})

def orderMsg(request):
    return render(request, "part4/orderMessage.html")

def desktop(request):
    desktopList = Desktop.objects.all()
    dekstopsDB = json.loads(json.dumps(list(desktopList.values()), cls=DjangoJSONEncoder))
    return render(request, "part4/desktop.html", {"desktops": dekstopsDB})

def desktopConfig(request, pk):
    # desktop = next(item for item in desktops if item["model"] == pk)
    desktop = Desktop.objects.get(model=pk)
    
    return render(request, "part4/desktopConfig.html", {"desktop": desktop})

def contact(request):

    return render(request, "part4/contact.html")

def search(request):
    results =[]

    if request.GET:
        model = request.GET.get("query")
        laptops = Laptop.objects.filter(model__contains = model)
        desktops = Desktop.objects.filter(model__contains = model)
        results = list(chain(laptops,desktops))

        return render(request, "part4/search.html", {"results": results})
    

def feedback(request):
    if(request.POST):

        Feedback.objects.create(
            email = request.POST.get("email"),
            message = request.POST.get("message")
        )
    
    return render(request, "part4/feedback.html")

def delete(request):
    context={}
    if not request.user.is_authenticated:
        return redirect("login")

   
    try:
        user = request.user
        logout(request)
        user.delete()
        context['msg'] = 'Bye Bye'
    except Exception as e: 
        context['msg'] = 'Something went wrong!'

    else:
        context['msg'] = 'Request method should be "DELETE"!'

    return render(request, "part4/main.html")


