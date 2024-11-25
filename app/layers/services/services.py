# Capa de servicio / lógica de negocio

from ..persistence import repositories
from ..utilities import translator
from django.contrib.auth import get_user

def getAllImages(input=None):
    """
    Obtiene un listado de imágenes de la API y las transforma en Cards.
    Si `input` está presente, filtra los resultados.
    """
    # TODO: Conectar con transport.py para obtener datos crudos desde la API.
    json_collection = []  # Simulación: Lista de datos crudos obtenidos de la API.

    # Transformamos los datos crudos en Cards (estructura asumida).
    images = []
    for data in json_collection:
        # TODO: Mapea `data` a una estructura Card (ejemplo simulado).
        card = {
            "name": data.get("name"),
            "status": data.get("status"),
            "image_url": data.get("image"),
            "last_location": data.get("last_location"),
            "first_seen": data.get("first_seen"),
        }
        images.append(card)

    # Filtrar imágenes si `input` está presente.
    if input:
        images = [img for img in images if input.lower() in img["name"].lower()]

    return images

def saveFavourite(request):
    """
    Guarda un personaje como favorito para el usuario autenticado.
    """
    if not request.user.is_authenticated:
        return None  # Evita guardar si el usuario no está autenticado.

    fav_data = request.POST.get('fav_data')  # Simulación: Datos del favorito desde el request.
    if fav_data:
        # Transformamos los datos en una estructura válida (ej. modelo "Card").
        fav = {
            "user": request.user,  # Asignamos el usuario actual.
            "data": fav_data,  # Datos relevantes del personaje.
        }
        return repositories.saveFavourite(fav)  # Guardamos en la base de datos.

    return None

def getAllFavourites(request):
    """
    Devuelve todos los favoritos del usuario autenticado.
    """
    if not request.user.is_authenticated:
        return []  # Usuario no autenticado: Lista vacía.

    user = get_user(request)  # Obtenemos el usuario actual.
    favourite_list = repositories.getAllFavourites(user)  # TODO: Implementar en `repositories.py`.
    
    mapped_favourites = []
    for favourite in favourite_list:
        # Transformamos cada favorito en una Card (simulado).
        card = {
            "id": favourite.get("id"),
            "name": favourite.get("name"),
            "image_url": favourite.get("image_url"),
        }
        mapped_favourites.append(card)

    return mapped_favourites

def deleteFavourite(request):
    """
    Elimina un favorito específico del usuario autenticado.
    """
    if not request.user.is_authenticated:
        return None  # Usuario no autenticado.

    fav_id = request.POST.get('id')  # ID del favorito a eliminar.
    if fav_id:
        return repositories.deleteFavourite(fav_id)  # Borramos favorito por ID.

    return None
