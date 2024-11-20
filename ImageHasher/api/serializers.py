from rest_framework import serializers
from .models import ImageRecord

class ImageRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageRecord
        fields = ['id', 'image_url', 'md5_hash', 'phash']
