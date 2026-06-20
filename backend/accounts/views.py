from random import randint
from urllib import request

from django.http import HttpRequest, HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import render, redirect

# Create your views here.
def index(request):

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.success(request, "There was an error with your login")
            return render(request, "accounts/index.html", {"error": "Invalid Login Credentials"})
    else:
        return render(request, "accounts/index.html", {"error": None})
    

