from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from django.contrib.auth.models import send_mail
from rest_framework.authtoken.models import Token

@receiver(signal=post_save, sender=get_user_model())
def create_api_token(sender, instance, created, **kwargs):
    if created:
        token = Token.objects.create(user=instance)
        token.save()


