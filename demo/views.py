from django.shortcuts import render
from .models import Image

def index(request):
    data = Image.objects.all()
    context = {
        'data':data
    }

    return render(request, 'demo/display.html', context)
