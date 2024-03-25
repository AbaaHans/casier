from django.contrib import admin
from .models import Utilisateur

from django.contrib.auth.admin import UserAdmin

from .forms import UtilisateurChangeForm , UtilisateurCreationForm


# Register your models here.
class UtilisateurAdmin(UserAdmin):
    add_form = UtilisateurCreationForm
    form = UtilisateurChangeForm
    model = Utilisateur
    list_display = ("pseudo", "is_staff", "is_active","is_superuser")
    list_filter = ("pseudo", "is_staff", "is_active","is_superuser")
    fieldsets = (
        (None, {"fields": ("nom","prenom","pseudo", "password")}),
        ("Permissions", {"fields": ("is_staff", "is_active", "is_superuser", "groups", "user_permissions")}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "nom","prenom","pseudo","password1", "password2", "is_staff",
                "is_active","is_superuser", "groups", "user_permissions"
            )}
        ),
    )
    search_fields = ("pseudo",)
    ordering = ("pseudo",)


admin.site.register(Utilisateur, UtilisateurAdmin)

