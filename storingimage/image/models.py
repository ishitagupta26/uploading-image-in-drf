
from django.db import models
from PIL import Image as PilImage
from io import BytesIO
from django.core.files.base import ContentFile


class Image(models.Model):
    original_image = models.ImageField(upload_to='images/')
    compressed_image = models.ImageField(upload_to='compressed_images/', null=True, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # Save the original image first

        if not self.id or self.original_image != Image.objects.get(id=self.id).original_image:
            self.compress_image()
            super().save(*args, **kwargs)  # Save the instance again with the compressed image

    def compress_image(self):
        with self.original_image.open() as image_file:
            image = PilImage.open(image_file)
            image_io = BytesIO()
            image.save(image_io, format='JPEG', quality=70)
            compressed_image_name = f'compressed_{self.original_image.name}'
            self.compressed_image.save(compressed_image_name, ContentFile(image_io.getvalue()), save=False)
