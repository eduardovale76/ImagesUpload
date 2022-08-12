from django.shortcuts import render, redirect
from .models import Image
from .forms import ImageUploadForm

def index(request):
    data = Image.objects.all()
    context = {
        'data':data
    }

    return render(request, 'demo/display.html', context)

def uploadView(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        context = {'form':form}
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ImageUploadForm()
        context = {'form':form}
    return render(request, 'demo/upload.html', context)