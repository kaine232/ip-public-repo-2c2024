# Capa de vista/presentación

from django.shortcuts import redirect, render
from .layers.services import services
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from app.layers.transport import transport
import json

def index_page(request):
    """Página de inicio."""
    return render(request, 'index.html')

# esta función obtiene 2 listados que corresponden a las imágenes de la API y los favoritos del usuario y los usa para dibujar el correspondiente template.
# Si el opcional de favoritos no está desarrollado, devuelve un listado vacío
def home(request):

    images = [] 
    for objeto in transport.getAllImages():
        images.append(objeto['image'])  # Asegúrate de que 'objeto' tiene una clave 'image'

    favourite_list = []  # Este listado se puede llenar más tarde con favoritos del usuario

    return render(request, 'home.html', {"images": images, "favourite_list": favourite_list})

def search(request):
    """
    Buscar personajes por nombre.
    """
    search_msg = request.POST.get('query', '')

    if search_msg:
        # TODO: Implementar lógica de búsqueda (consultar API o base de datos)
        pass
    else:
        return redirect('home')

@login_required
def getAllFavouritesByUser(request):
    """
    Obtiene los favoritos de un usuario logueado.
    """
    favourite_list = []  # TODO: Obtener de la base de datos
    return render(request, 'favourites.html', {"favourite_list": favourite_list})

@login_required
def saveFavourite(request):
    """
    Guarda un personaje en favoritos.
    """
    # TODO: Implementar funcionalidad para guardar en base de datos
    pass

@login_required
def deleteFavourite(request):
    """
    Elimina un personaje de los favoritos.
    """
    # TODO: Implementar funcionalidad para eliminar en base de datos
    pass

@login_required
def exit(request):
    """
    Cierra sesión y redirige a la página de inicio.
    """
    logout(request)
    return redirect('index_page')

