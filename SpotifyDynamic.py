import spotipy
import random
import json
from spotipy.oauth2 import SpotifyOAuth

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET_CODE",
    redirect_uri="http://localhost:8888/callback",
    scope="playlist-modify-public playlist-modify-private user-library-read"
), requests_timeout=20)

print("Autenticación exitosa. ¡Estás listo para interactuar con Spotify!")

def obtener_canciones_favoritas():
    canciones = cargar_canciones()
    
    if not canciones: 
        print("No se encontraron canciones guardadas. Obteniendo canciones favoritas desde la API...")
        canciones = []
        resultados = sp.current_user_saved_tracks(limit=30)
        while resultados:
            canciones += resultados["items"]
            resultados = sp.next(resultados) if resultados["next"] else None
        print(f"Se encontraron {len(canciones)} canciones favoritas.")
        guardar_canciones(canciones) 
    else:
        print(f"Se cargaron {len(canciones)} canciones favoritas desde el archivo JSON.")
    
    return canciones

def filtrar_por_genero(canciones):
    generos_canciones = {}
    for item in canciones:
        track = item["track"]
        artistas = track["artists"]
        for artista in artistas:
            try:
                artista_info = sp.artist(artista["id"])
                generos = artista_info.get("genres", [])
                for genero in generos:
                    if genero not in generos_canciones:
                        generos_canciones[genero] = []
                    generos_canciones[genero].append(track["id"])
            except Exception as e:
                print(f"Error al obtener información del artista {artista['name']}: {e}")

    generos_canciones = {genero: canciones for genero, canciones in generos_canciones.items() if len(canciones) >= 10}
    print(f"Se encontraron {len(generos_canciones)} géneros con al menos 10 canciones.")
    return generos_canciones

def seleccionar_genero_aleatorio(generos_canciones):
    if not generos_canciones:
        print("No se encontraron géneros en tus canciones.")
        return None, []
    genero_aleatorio = random.choice(list(generos_canciones.keys()))
    canciones_del_genero = generos_canciones[genero_aleatorio]
    print(f"Género seleccionado: {genero_aleatorio} ({len(canciones_del_genero)} canciones).")
    return genero_aleatorio, canciones_del_genero

def obtener_playlist_fija(sp):
    playlists = sp.current_user_playlists()
    for playlist in playlists['items']:
        if playlist['name'].startswith("Dynamic Playlist"):
            return playlist['id']
    print("No se encontró una playlist fija, creando 'Dynamic Playlist'...")
    playlist = sp.user_playlist_create(sp.current_user()['id'], "Dynamic Playlist", public=True)
    return playlist['id']

def actualizar_playlist_dinamica(genero, canciones_del_genero):
    playlist_id = obtener_playlist_fija(sp)
    
    genero_titulo = genero.title() 
    nuevo_nombre = f"Dynamic Playlist: {genero_titulo}"
    sp.playlist_change_details(playlist_id, name=nuevo_nombre)
    print(f"El nombre de la playlist se actualizó a '{nuevo_nombre}'.")
    
    print(f"Limpiando y añadiendo {len(canciones_del_genero)} canciones del género '{genero_titulo}'...")
    sp.playlist_replace_items(playlist_id, []) 
    for i in range(0, len(canciones_del_genero), 100):
        bloque_canciones = canciones_del_genero[i:i+100]
        sp.playlist_add_items(playlist_id, bloque_canciones)
        print(f"Bloque de {len(bloque_canciones)} canciones añadido a la playlist.")

def guardar_canciones(canciones):
    with open('canciones_favoritas.json', 'w') as f:
        json.dump(canciones, f)
    print("Canciones favoritas guardadas en 'canciones_favoritas.json'.")

def cargar_canciones():
    try:
        with open('canciones_favoritas.json', 'r') as f:
            canciones = json.load(f)
        print("Canciones favoritas cargadas desde 'canciones_favoritas.json'.")
        return canciones
    except FileNotFoundError:
        print("No se encontró el archivo de canciones favoritas, obteniéndolas de nuevo...")
        return None

def guardar_generos(generos_canciones):
    with open('generos_filtrados.json', 'w') as f:
        json.dump(generos_canciones, f)
    print("Géneros guardados en 'generos_filtrados.json'.")

def cargar_generos():
    try:
        with open('generos_filtrados.json', 'r') as f:
            generos_canciones = json.load(f)
        print("Géneros cargados desde 'generos_filtrados.json'.")
        return generos_canciones
    except FileNotFoundError:
        print("No se encontró el archivo de géneros, filtrando de nuevo...")
        return None

if __name__ == "__main__":
    print("Obteniendo tus canciones favoritas...")
    canciones_favoritas = obtener_canciones_favoritas()
    
    print("Cargando géneros filtrados...")
    generos_canciones = cargar_generos()
    
    if not generos_canciones:
        print("Filtrando canciones por género...")
        generos_canciones = filtrar_por_genero(canciones_favoritas)
        guardar_generos(generos_canciones) 
    
    print("Seleccionando un género al azar...")
    genero, canciones_del_genero = seleccionar_genero_aleatorio(generos_canciones)
    
    if genero:
        print("Creando o actualizando playlist dinámica...")
        actualizar_playlist_dinamica(genero, canciones_del_genero)
