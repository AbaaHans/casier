from django import forms
from .models import CasierJudiciaire
from django.core.validators import FileExtensionValidator, RegexValidator

class CasierJudiciareForm(forms.ModelForm):
    telephone_regex=RegexValidator(regex=r'^\+?1?\d{8,15}$', message="Le numero doit être du format: '+999999999'. 15 chiffres autorisés.")
    file_extensions= FileExtensionValidator(message="Seul les fichiers d'extension de type jpeg, png, jpg, pdf sont autorisés.",allowed_extensions=["jpeg","png","jpg","pdf"])
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

        error_messages = {
            'nom' : {
                'required' : 'Le champ votre Nom est requis.'
            },
            'prenom' : {
                'required' : 'Le champ votre Prenom est requis.'
            },
            'nom_pere' : {
                'required' : 'Le champ Nom et prénom du père est requis.'
            },
            'nom_mere' : {
                'required' : 'Le champ Nom et prénom de la mère est requis.'
            },
            'date_naisance' : {
                'required' : 'Le champ Date de Naissance est requis.'
            },
             'lieu_naissance' : {
                'required' : 'Le champ Date de Naissance est requis.'
            },
             'pays' : {
                'required' : 'Le champ Lieu de Naissance est requis.'
            },
             'nationalite' : {
                'required' : 'Le champ Nationalité est requis.'
            },
             'profession' : {
                'required' : 'Le champ Profession est requis.'
            },
             'etat_familiale' : {
                'required' : 'Le champ Etat civil est requis.'
            },
             'adresse' : {
                'required' : 'Le champ Adresse est requis.'
            },
             'genre' : {
                'required' : 'Le champ Genre est requis.'
            },
             'telephone' : {
                'required' : 'Le champ Telephone est requis.'
            },
             'piece_justificatif' : {
                'required' : 'Le champ Pièce justificative est requis.',
                'invalid' : "Seul les fichiers d'extension de type jpeg, png, jpg, pdf sont autorisés."
            },
            
        }

    def __init__(self, *args, **kwargs):
        super(CasierJudiciareForm, self).__init__(*args, **kwargs)
        self.fields['piece_justificatif'].validators.append(self.file_extensions)
        self.fields['telephone'].validators.append(self.telephone_regex)