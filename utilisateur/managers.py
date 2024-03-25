from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _

class UtilisateursManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, pseudo, password, **extra_fields):
        """
        Creates and saves a User with the given pseudo and password.
        """
        if not pseudo:
            raise ValueError('The given pseudo must be set')
        pseudo = self.normalize_email(pseudo)
        user = self.model(pseudo=pseudo, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, pseudo, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(pseudo, password, **extra_fields)

    def create_superuser(self, pseudo, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True."))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))

        return self._create_user(pseudo, password, **extra_fields)