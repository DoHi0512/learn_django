from django.shortcuts import render
from .models import Photo
# Create your views here.


def photo_list(request):
    photo = Photo.objects.all()
    return render(request, 'photo/photo_list.html', {'photos' : photo})
