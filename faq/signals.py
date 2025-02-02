from django.core.cache import cache
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import FAQ  # Import your FAQ model


@receiver(post_save, sender=FAQ)
def clear_cache(sender, instance, **kwargs):
    cache.clear()  # Clears all cache when a new FAQ is added/updated
