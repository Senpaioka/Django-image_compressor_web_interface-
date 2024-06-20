from django.shortcuts import render, redirect
from img_compression.forms import ImgCompressForms
from PIL import Image
import io
import imghdr

# Create your views here.

def img_compress(request):
    
    if request.method == "POST":
        # getting the request
        get_form = ImgCompressForms(request.POST, request.FILES)
        # validating the request
        if get_form.is_valid():
            submitted_img = get_form.cleaned_data['original_img']
            submitted_quality = get_form.cleaned_data['compression_quality']

            form_obj = get_form.save(commit=False)

        # finding out image format

            img_format = imghdr.what(submitted_img)

        # doing actual compression
            compressed_file_name = str(f'compressed_{submitted_img}')

            img = Image.open(submitted_img)
            buffer = io.BytesIO()
            img.save(buffer, format=img_format ,quality=submitted_quality)
            buffer.seek(0)

        # save to the database

            form_obj.compressed_img.save(
                compressed_file_name,
                buffer
            )

        # redirect 

            return redirect('img_compress')

    else:
        get_form = ImgCompressForms()

    
    context = {
        'form_content' : get_form,
    }

    return render(request, 'home.html', context)