from django.db import models

class ImageRecord(models.Model):
    image_url = models.URLField()
    md5_hash = models.CharField(max_length=32)
    phash = models.CharField(max_length=16)
    
    def __str__(self):
        return self.image_url
