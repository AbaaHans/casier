from django.shortcuts import render,redirect
from django.http.request import HttpRequest
from casierjudiciaire.forms import CasierJudiciareForm
from casierjudiciaire.models import CasierJudiciaire
from django.contrib import messages
from casierjudiciaire.utilitaires import genererCodeSuivie


def index(request:HttpRequest):
    return render(request, 'index.html')


def connexion(request:HttpRequest):
    return render(request, 'connexion.html')

def demandecasier(request:HttpRequest):
    if request.method == "GET":
        form = CasierJudiciareForm()
        return render(request,"demandecasier.html",{"form":form})
    elif request.method == "POST":
        form = CasierJudiciareForm(request.POST, request.FILES)
        if form.is_valid():
            #Generer le numero de la demande
            code_suivi_demande = genererCodeSuivie()
            demande : CasierJudiciaire = form.save(commit=False)
            demande.code_demande = code_suivi_demande
            demande.save()

            return render(request, "succesdemande.html",{"code_suivi":code_suivi_demande})
        else:
            return render(request,"demandecasier.html",{"form":form})
    else:
        return redirect("index")
    

def suivicasier(request:HttpRequest):
    if request.method == "GET":
        return render(request,"suivicasier.html")
    elif request.method == "POST":
        data = request.POST
        code_suivi_demande = data.get("numeroSuiviCasier")

        if code_suivi_demande is None:
            messages.error(request, "Le numero de suivi est requis.")
            return redirect("suivicasier")

        if len(str(code_suivi_demande)) <= 0:
            messages.error(request, "Le numero de suivi est ne peut pas être vide.")
            return redirect("suivicasier")
        
        try :
            code_suivi_demande = int(code_suivi_demande)
            if code_suivi_demande <= 0:
                messages.error(request, "Le numero de suivi est ne peut pas être negatif ou nul.")
                return redirect("suivicasier")
            
            if code_suivi_demande > 99999999:
                messages.error(request, "Le numero de suivi ne peut depasser 99999999.")
                return redirect("suivicasier")
               
            demande = CasierJudiciaire.objects.get(code_demande=code_suivi_demande)
            return render(request,"suivicasiersucces.html",{"demande":demande,"code_suivi":code_suivi_demande})
        except CasierJudiciaire.DoesNotExist:
            messages.error(request, "Aucune demande de casier judiciare correspondate n'a trouvé pour ce numero de suivi.")
            return redirect("suivicasier")
        except ValueError:
            messages.error(request, "Le numero de suivi doit forcement être numerique.")
            return redirect("suivicasier")
        except:
            messages.error(request, "Une erreur de traitement est survenue.")
            return redirect("suivicasier")
    else:
        return redirect("index")