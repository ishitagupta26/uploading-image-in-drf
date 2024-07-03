

from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Image


@receiver(post_save, sender=Image)
def compress_image_signal(sender, instance, **kwargs):
    if instance.original_image and not instance.compressed_image:
        instance.compress_image()
        instance.save()
