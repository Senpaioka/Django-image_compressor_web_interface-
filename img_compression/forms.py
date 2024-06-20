# from django import forms

# class ImgCompressForms(forms.Form):
#     img_field = forms.ImageField(label="Select Image :")
#     quality_field = forms.IntegerField(label="Image Quality :")

from django.forms import ModelForm
from img_compression.models import ImageCompression

class ImgCompressForms(ModelForm):
    
    class Meta:
        model =  ImageCompression
        fields = ['original_img', 'compression_quality']
