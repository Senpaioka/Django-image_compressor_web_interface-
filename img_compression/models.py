from django.db import models
from io import BytesIO
from PIL import Image

# Create your models here.

class ImageCompression(models.Model):
    QUALITY_CHOICES = [(value, value) for value in range(10, 101, 10)]

    original_img = models.ImageField(upload_to='original_img/')
    compressed_img = models.ImageField(upload_to='compressed_img/')
    compression_quality = models.IntegerField(choices=QUALITY_CHOICES)
    compressed_at = models.DateTimeField(auto_now_add=True)



    