from django.dispatch import receiver
from django.core.cache import cache
from django.db.models.signals import pre_save, post_save
from django.db.models import Q

from .system_settings import SystemSettings


@receiver(post_save, sender=SystemSettings)
def update_system_settings(sender, instance, created, *args, **kwargs):
    if created:
        cache.clear() # clear cached settings
        old_settings = SystemSettings.objects.all().exclude(id=instance.id)
        for setting in old_settings:
            setting.delete()

