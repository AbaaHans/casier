from django.shortcuts import render,redirect
from django.http.request import HttpRequest
from casierjudiciaire.forms import CasierJudiciareForm



def index(request:HttpRequest):
    return render(request, 'index.html')


def connexion(request:HttpRequest):
    return render(request, 'connexion.html')


def demandecasier(request:HttpRequest):
    if request.method == "GET":
        form = CasierJudiciareForm()
        return render(request,"demandecasier.html",{"form":form})
    elif request.method == "POST":
        pass
    else:
        return redirect("index")