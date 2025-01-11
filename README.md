# Dynamic Spotify Playlist Generator
<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/1/19/Spotify_logo_without_text.svg/1200px-Spotify_logo_without_text.svg.png" width="200" />

🎵 **Generador Dinámico de Playlist en Spotify** 🎶

Este proyecto personal utiliza la API de Spotify para crear una **playlist dinámica** a partir de las canciones favoritas del usuario. El script selecciona géneros de música aleatorios, filtra los géneros con al menos 10 canciones, y actualiza o crea una nueva playlist en Spotify con canciones del género seleccionado. 

## 🚀 Características 

- **Autenticación segura** con Spotify mediante OAuth.
- **Filtrado de géneros**: Solo géneros con al menos 10 canciones favoritas.
- **Creación o actualización** de una playlist llamada "Dynamic Playlist". 
- **Automatización diaria** a través de GitHub Actions para generar una nueva playlist cada día.

## 🔧 Requisitos

Para poder usar este proyecto, necesitas tener lo siguiente:
 
- Una cuenta de **Spotify**.
- Un proyecto creado en [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/applications) para obtener tus credenciales de la API.
## 🛠️ Instalación
Clona el repositorio:
```bash
git clone https://github.com/tu_usuario/spotify-dynamic-playlist.git
cd spotify-dynamic-playlist
```
Instala las dependencias:
```bash
pip install -r requirements.txt
```
Ejecuta el script:
```bash
python SpotifyDynamic.py
```
## 📜 Uso
Una vez que hayas configurado las credenciales API dentro del script e instalado las dependencias, simplemente ejecuta el script.
## ⚙️ Flujo de Trabajo
El script obtiene las canciones favoritas del usuario.
Filtra los géneros que tienen al menos 10 canciones.
Selecciona un género aleatorio y actualiza la playlist "Dynamic Playlist".
Si la playlist no existe, la crea automáticamente.
## 🔑 Autenticación
Este proyecto utiliza Spotify OAuth para autenticar al usuario. Asegúrate de haber configurado correctamente tus credenciales de cliente en el Spotify Developer Dashboard y de haber autorizado el acceso a tu cuenta de Spotify.

## 📅 Programación Automática
Este proyecto está configurado para ejecutarse automáticamente todos los días a medianoche (horario UTC), lo que te permitirá disfrutar siempre de una playlist actualizada con un nuevo género aleatorio cada día.
