from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="accueil"),
    path('<int:id>',views.contenu_album,name="Lire contenu album"),


]