# Dynamic Spotify Playlist Generator
<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/1/19/Spotify_logo_without_text.svg/1200px-Spotify_logo_without_text.svg.png" width="200" />

🎵 **Dynamic Spotify Playlist Generator** 🎶

This personal project uses the Spotify API to create a **dynamic playlist** based on the user's favorite songs. The script selects random music genres, filters genres with at least 10 songs, and updates or creates a new playlist on Spotify with songs from the selected genre.

## 🚀 Features

- **Secure authentication** with Spotify using OAuth.
- **Genre filtering**: Only genres with at least 10 favorite songs.
- **Creation or update** of a playlist named "Dynamic Playlist."
- **Daily automation** via GitHub Actions to generate a new playlist every day.

## 🔧 Requirements

To use this project, you need the following:

- A **Spotify** account.
- A project created on the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/applications) to obtain your API credentials.

## 🛠️ Installation

Clone the repository:
```
git clone https://github.com/your_username/spotify-dynamic-list.git
cd spotify-dynamic-list
```
Install dependencies:
```
pip install -r requirements.txt
```
Run the script:
```
python SpotifyDynamic.py
```
## 📜 Usage
Once you've set up the API credentials within the script and installed the dependencies, simply run the script.

## ⚙️ Workflow
The script fetches the user's favorite songs.
Filters genres that have at least 10 songs.
Selects a random genre and updates the "Dynamic Playlist."
If the playlist does not exist, it creates it automatically.
## 🔑 Authentication
This project uses Spotify OAuth to authenticate the user. Make sure to correctly configure your client credentials in the Spotify Developer Dashboard and authorize access to your Spotify account.

## 📅 Automated Scheduling
This project is set to run automatically every day at midnight (UTC), ensuring you always have an updated playlist featuring a new random genre daily.
