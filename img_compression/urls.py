
from django.urls import path
from img_compression import views

urlpatterns = [
    path('', views.img_compress, name="img_compress"),
]
