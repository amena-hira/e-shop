from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import auth, User
import urllib.parse
import requests

from django.contrib import messages
from django.contrib.auth.models import auth, User


# from amazon.paapi import AmazonAPI

# Create your views here.


def homeView(request):
    return render(request, 'index.html')

# def Search(request):
    
#     amazon = AmazonAPI(KEY, SECRET, TAG, COUNTRY)
#     search_item = request.GET['search_item']
#     search_item.replace('','%20')

#     product = amazon.search_products(item_count=25, keywords=search_item)

#     #url = 'https://price-api.datayuge.com/api/v1/compare/search?product=' + search_item + '&api_key=KbOT10p5lD62PTyUvDiBOGF2uQgj1f7xN88'
#     url = product.url
#     products = requests.get(url).json()
#     return render (request, 'products.html', {'products': products})

def register(request):

    if request.method == 'POST':
        first_name  = request.POST['first_name']
        last_name   = request.POST['last_name']
        username    = request.POST['username']
        email       = request.POST['email']
        password    = request.POST['password1']
        password2   = request.POST['password2']

        if password == password2:
            if User.objects.filter(username = username).exists():
                messages.error(request, 'Username is already taken.')
                return redirect('/')

            elif User.objects.filter(email = email).exists():
                messages.error(request, 'The email is already registerd.')
            
            else:
                user = User.objects.create_user(username = username, password = password, email = email, first_name = first_name, last_name = last_name)
                user.save()
                return redirect('/')    
        else:
            messages.error(request, 'Password doen\'t match.')
    else:
        return render(request, 'register.html')


def login(request):
    if request.method == 'POST':
        username    = request.POST['username']
        password    = request.POST['password']

        user = auth.authenticate(username = username, password = password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')    
        else:
            messages.error(request, 'Invalid username or password')
            return redirect('login')
    else:
        if request.user.is_authenticated:
            return redirect('/')
        else:
            return render(request, 'login.html')

    

def logout(request):
    auth.logout(request)
    return redirect('/')        