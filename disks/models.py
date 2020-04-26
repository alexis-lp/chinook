from django.db import models

# Create your models here.

class Album(models.Model):
    title = models.CharField(max_length=160,verbose_name="Nom")
    artist = models.ForeignKey('Artist', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Artist(models.Model):
    name = models.CharField(max_length=120,verbose_name="Nom")

    def __str__(self):
        return self.name

class Track(models.Model):
    name = models.CharField(max_length=200,verbose_name="Titre")
    album = models.ForeignKey('Album', on_delete=models.CASCADE)
    composer = models.CharField(max_length=200,verbose_name="Compositeur")
    milliseconds = models.TextField(verbose_name="Durée")
    bytes = models.IntegerField(verbose_name="Poids")
    unitPrice = models.DecimalField(max_digits=10, decimal_places=2,verbose_name="Prix")

    def __str__(self):
        return self.name

