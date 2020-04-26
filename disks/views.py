from django.shortcuts import render
from disks.models import *
from django.shortcuts import render,redirect, get_object_or_404


# Create your views here.

def home(request):
    albums = Album.objects.all()
    return render(request,'disks/accueil.html',{'list_albums': albums})

def contenu_album(request,id):
    albums = Album.objects.all()
    album = Album.objects.get(id=id)
    titres = Track.objects.filter(album=album)
    return render(request,'disks/details_album.html',{'list_albums': albums, 'album':album,'titres_de_l_album':titres})
