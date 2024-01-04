import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import pprint

spotify_client_id="111676cd96344465b89b5c233b75e2fd"
spotify_client_secret="a36c837873fd424fb95696d6afb38980"

date_pref=input("Which year do you want to travel to? Type the data in this format YYYY-MM-DD: ")

response=requests.get(f"https://www.billboard.com/charts/hot-100/{date_pref}")
billboard_web=response.text

soup=BeautifulSoup(billboard_web,'html.parser')
all_songs=[song.getText().replace("\n","") for song in soup.select("li #title-of-a-story")]

sp=spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=spotify_client_id,
        client_secret=spotify_client_secret,
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id=sp.current_user()["id"]
print(user_id)

song_uris = []
year = date_pref.split("-")[0]
for song in all_songs:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

#Creating a new private playlist in Spotify
playlist = sp.user_playlist_create(user=user_id, name=f"{date_pref} Billboard 100", public=False)
print(playlist)

#Adding songs found into the new playlist
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
