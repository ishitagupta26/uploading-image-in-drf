from rest_framework import serializers
from .models import Image


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['id', 'original_image', 'compressed_image', 'uploaded_at']
        read_only_fields = ['id', 'compressed_image', 'uploaded_at']