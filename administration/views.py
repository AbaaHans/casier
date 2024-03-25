from django.shortcuts import render,redirect
from django.http.request import HttpRequest
from  django.contrib import messages
# Create your views here.


def index(request:HttpRequest):
    if request.method == "GET":
        if request.user.is_authenticated:
            return render(request,'dashboard/index.html')
        else:
            messages.error(request,"Veuillez-vous connecter.")
            return redirect("connexion")
    else:
        return redirect("index")

