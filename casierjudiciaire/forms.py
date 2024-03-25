from django import forms
from .models import CasierJudiciaire


class CasierJudiciareForm(forms.ModelForm):
    class Meta:
        model = CasierJudiciaire
        fields = ["nom","prenom","nom_pere","nom_mere","date_naisance","lieu_naissance","pays","nationalite",
                  "profession","etat_familiale","adresse","telephone","piece_justificatif","genre"]
        
        widgets={
            'nom' : forms.TextInput(attrs={'class':"form-control"}),
            'prenom' : forms.TextInput(attrs={'class':"form-control"}),
            'nom_pere' : forms.TextInput(attrs={'class':"form-control"}),
            'nom_mere' : forms.TextInput(attrs={'class':"form-control"}),
            'date_naisance': forms.TextInput(attrs={'class':"form-control",'type':"date"}),
            'lieu_naissance' : forms.TextInput(attrs={'class':"form-control"}),
            'pays' : forms.Select(attrs={'class':"form-control"}),
            'nationalite' : forms.Select(attrs={'class':"form-control"}),
            'profession' : forms.Select(attrs={'class':"form-control"}),
            'etat_familiale' : forms.Select(attrs={'class':"form-control"}),
            'adresse' : forms.TextInput(attrs={'class':"form-control"}),
            'telephone' : forms.TextInput(attrs={'class':"form-control"}),  
            'genre' : forms.Select(attrs={'class':"form-control"}),
            'piece_justificatif' : forms.FileInput(attrs={'class':"form-control"}),  
        }


        #Il manque la ville dans le model
        labels = {
            'nom' : 'Entrez votre nom',
            'prenom': 'Entrez votre prénom',
            'nom_pere': 'Nom et prénom du père',
            'nom_mere': 'Nom et prénom de la mère',
            'date_naisance' : 'Date de Naissance',
            'lieu_naissance' : 'Lieu de naissance',
            'pays' : 'Pays de naissance',
            'nationalite' : 'Nationalité',
            'profession' :  'Profession',
            'etat_familiale' : 'Etat civil',
            'adresse' : 'Entrez votre adresse avec la ville',
            'genre' : 'Genre',
            'telephone' : 'Numéro de téléphone',
            'piece_justificatif' : 'Pièce justificative en votre posséssion'
        }