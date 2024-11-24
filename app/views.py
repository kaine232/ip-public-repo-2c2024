# capa de vista/presentación

from django.shortcuts import redirect, render
from .layers.services import services
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from app.layers.transport import transport
import json

def index_page(request):
    return render(request, 'index.html')

# esta función obtiene 2 listados que corresponden a las imagenes de la API y los favoritos del usuario y los usa para dibujar el correspondiente template.
#si el opcional de favoritos no está desarrollado devuelve un listado vacio 
def home(request):

    images = [] 
    for objeto in transport.getAllImages():
        images.append(objeto['image'])

    favourite_list = []

    return render(request, 'home.html', {"images": images, "favourite_list": favourite_list})

# Buscar personajes (pendiente de implementación)
def search(request):
    search_msg = request.POST.get('query', '')

    if search_msg != '':
        # Implementar la lógica de búsqueda
        pass
    else:
        return redirect('home')

# Favoritos (funcionalidades relacionadas con el usuario logueado)
@login_required
def getAllFavouritesByUser(request):
    favourite_list = []
    return render(request, 'favourites.html', {"favourite_list": favourite_list})

@login_required
def saveFavourite(request):
    pass

@login_required
def deleteFavourite(request):
    pass

@login_required
def exit(request):
    pass