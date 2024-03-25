from django.shortcuts import render,redirect
from django.http.request import HttpRequest
from  django.contrib import messages
from django.core.validators import validate_email

from django.contrib.auth import login,authenticate,logout

# Create your views here.

def authentificate_user(request:HttpRequest):
    if request.method == "POST":
        data = request.POST
        
        pseudo = data.get("pseudo")
        mdp = data.get("mdp")

        if pseudo is None:
            messages.error(request, "Le champ Adresse email est obligatoire.")
            return redirect("connexion")
        if mdp is None:
            messages.error(request, "Le champ Mot de passe est obligatoire.")
            return redirect("connexion")
        
        if len(str(pseudo).strip()) <= 0:
            messages.error(request, "Le champ Adresse email ne peut pas être vide.")
            return redirect("connexion")
        
        if len(str(mdp).strip()) <= 0:
            messages.error(request, "Le champ Mot de passe ne peut pas être vide.")
            return redirect("connexion")
        
        pseudo = str(pseudo).strip().lower()
        
        try:
            validate_email(pseudo)
        except:
            messages.error(request, "Cette Adresse email n'est pas un adresse email valide.")
            return redirect("connexion")
        

        user = authenticate(request,username=pseudo,password=mdp)

        if user is None:
            messages.error(request, "Les informations saisies sont incorrectes.")
            return redirect("connexion")
        else:
            login(request,user)
            return redirect("Dashboard:index")
    else:
        return redirect("connexion")
    

def deconnexion(request):
    logout(request)
    messages.success(request,"Vous avez bien été déconnecté(e)")
    return redirect("connexion")
