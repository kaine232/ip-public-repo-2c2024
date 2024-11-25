# Capa de vista/presentación

from django.shortcuts import redirect, render
from .layers.services import services
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

def index_page(request):
    """Página de inicio."""
    return render(request, 'index.html')

def home(request):
    """
    Página principal:
    Lista personajes y favoritos del usuario.
    """
    # Ejemplo de personajes (esto debería venir de una API o base de datos)
    characters = [
        {
            "name": "Rick Sanchez",
            "status": "Alive",
            "url": "https://example.com/rick.png",  # Reemplazar con URLs dinámicas o configuración
            "last_location": "Tierra C-137",
            "first_seen": "Pilot",
        },
        {
            "name": "Morty Smith",
            "status": "Dead",
            "url": "https://example.com/morty.png",
            "last_location": "Dimensión Cronenberg",
            "first_seen": "Pilot",
        },
        {
            "name": "Birdperson",
            "status": "Unknown",
            "url": "https://example.com/birdperson.png",
            "last_location": "Planeta Fénix",
            "first_seen": "Ricksy Business",
        },
    ]

    # Lista de favoritos (vacía si no implementada)
    favourite_list = []  # TODO: Reemplazar con lógica para obtener favoritos

    return render(request, 'home.html', {
        "characters": characters,
        "favourite_list": favourite_list,
    })

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
