from disks.models import *
from django.shortcuts import render,redirect, get_object_or_404
from .forms import SearchForm

# Create your views here.

def home(request):
    form = SearchForm(request.POST or None)
    album_recherche= "";
    if form.is_valid():
        album_recherche = form.cleaned_data['album']

    if album_recherche:
        albums = Album.objects.filter(title__contains=album_recherche)
    else:
        albums = Album.objects.all()

    return render(request,'disks/accueil.html',{'list_albums': albums,'album_recherche': album_recherche, "form": form})

def contenu_album(request,id):
    form = SearchForm(request.POST or None)
    album_recherche = "";
    if form.is_valid():
        album_recherche = form.cleaned_data['album']

    if album_recherche:
        albums = Album.objects.filter(title__contains=album_recherche)
    else:
        albums = Album.objects.all()


    album = Album.objects.get(id=id)
    titres = Track.objects.filter(album=album)
    return render(request,'disks/details_album.html',{'list_albums': albums, 'album': album, 'titres_de_l_album': titres, 'album_recherche': album_recherche, "form": form})
