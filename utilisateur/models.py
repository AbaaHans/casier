from django.db import models

from django.contrib.auth.models import AbstractBaseUser , PermissionsMixin

from django.utils.translation import gettext_lazy as _
from .managers import UtilisateursManager
# Create your models here.


class Utilisateur(AbstractBaseUser,PermissionsMixin):
    nom = models.CharField(_('Nom'),max_length=255)
    prenom = models.CharField(_('Prenom'),max_length=255)
    pseudo = models.EmailField(_('Courriel Personnel'), unique=True)
    is_active = models.BooleanField(_('Compte Active'), default=True)
    is_staff = models.BooleanField(default=False)

    objects = UtilisateursManager()

    USERNAME_FIELD = 'pseudo'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('Utilisateur')
        verbose_name_plural = _('Utilisateurs')
