# capa de vista/presentación

from django.shortcuts import redirect, render
from .layers.services import services
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

def index_page(request):
    return render(request, 'index.html')

# Home: Lista de personajes y favoritos
def home(request):
    characters = [
        {
            "name": "Rick Sanchez",
            "status": "Alive",
            "url": "https://example.com/rick.png",
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

    # Lista de favoritos (vacía por ahora)
    favourite_list = []

    return render(request, 'home.html', {"characters": characters, "favourite_list": favourite_list})

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
