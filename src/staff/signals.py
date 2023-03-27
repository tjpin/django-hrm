from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.hashers import make_password

from src.account.models import AccountUser
from .models import Staff


@receiver(post_save, sender=Staff)
def create_staff_user(sender, instance, created, *args, **kwargs):
    if created:
        name = f"{instance.first_name}_{instance.last_name}".lower()
        pass_string = f"{instance.first_name}.{str(instance.dob.year)}".lower()
        password = make_password(pass_string, hasher='default')
        
        user = AccountUser(
                username=name,
                email=instance.email,
                first_name=instance.first_name,
                last_name=instance.last_name,
                password=password,
                is_staff=True,
                is_superuser=False if not instance.is_admin else True,
            )
        user.save()
