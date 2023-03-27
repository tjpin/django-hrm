from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _


class AccountUserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError(_("Email address is required"))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_("is_staff must be = True"))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_("is_superuser must be = True"))
        
        return self.create_user(email, password, **extra_fields)
        
